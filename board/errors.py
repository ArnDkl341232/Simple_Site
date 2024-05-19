from flask import render_template , current_app

def page_not_found(e):
    current_app.logger.info(e)
    return render_template('errors/404.html', error="Break the screen"), 404

