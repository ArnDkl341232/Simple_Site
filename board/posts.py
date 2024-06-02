from flask import (Blueprint, render_template, request, redirect, url_for, current_app)

from exemple_file_openai import  AI

from board.database import get_db

bp = Blueprint("posts", __name__)

@bp.route("/create",methods = ("GET" , "POST"))
def create():
    if request.method == "POST":
        if request.form["author"] == "AI".lower():
            author = "AI"
            message = AI(request.form["message"])
        else:
            author = request.form["author"] or "NoName"
            message = AI(request.form["message"])

        if message:
            db = get_db()
            db.execute("INSERT INTO post (author, message) VALUES (?, ?)",
                       (author, message)
                       )
            db.commit()

            current_app.logger.info(f"New post by {author}")
            return redirect(url_for("posts.posts",notification = "Post created"))


    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    db = get_db()
    notification = request.args.get('notification')
    print('notification')
    posts = db.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    )
    return render_template("posts/posts.html", posts = posts , notification = notification)