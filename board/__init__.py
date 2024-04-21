# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello world"
#
# if __name__  == "__main__":
#     app.run(host = "0.0.0.0", port=8000, debug=True)



from flask import Flask
from board import pages
from board import posts
def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    return app

