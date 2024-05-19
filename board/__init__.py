from flask import Flask
from board import pages, posts, database, errors
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    database.init_app(app)
    app.config.from_prefixed_env()
    app.logger.setLevel("ERROR")

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404,errors.page_not_found)

    print(f"Current ENVIROMENT: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('ENVIRONMENT')}")

    return app

