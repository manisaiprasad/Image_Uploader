from flask import Flask, request, jsonify, redirect, url_for, make_response
from flask_cors import CORS, cross_origin
import logging
from flask import send_from_directory
from requests import Response
from . import db, post

app = Flask(__name__)
CORS(app, support_credentials=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@localhost:5432/interview",
)

UPLOAD_FOLDER = 'flask_server/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule(
    "/uploads/<filename>", endpoint="download_file", build_only=True
)

app.register_blueprint(post.bp)


@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)


@app.route('/api/hello')
def hello():
    return 'Hello World!'


@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.after_request
def after_request(response: Response) -> Response:
    response.access_control_allow_origin = "*"
    return response


db.init_app(app)

if __name__ == '__main__':
    app.run(ssl_context=("cert.pem", "key.pem"), debug=True, port=6000)
