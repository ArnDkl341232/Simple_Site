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
from board import pages , posts , database
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    database.init_app(app)
    app.config.from_prefixed_env()

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    print(f"Current ENVIROMENT: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('ENVIRONMENT')}")

    return app

