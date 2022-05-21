from flask import Blueprint, redirect, request, url_for, jsonify
from werkzeug.utils import secure_filename
from curses import flash
import logging
import os
from time import time
from PIL import Image
from flask_marshmallow import Marshmallow
from .db import Post, db

bp = Blueprint("post", __name__, url_prefix="/")

UPLOAD_FOLDER = 'flask_server/static/uploads'


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Image tiled 90 degrees to left
def rotate_image(image):
    img = Image.open(image)
    img = img.rotate(90)
    return img


@bp.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@bp.route("/api/upload", methods=["POST"])
def post_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    try:
        logger.info("request: {}".format(request))
        if not os.path.isdir(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)
        file = request.files['file']
        logger.info("request.files: {}".format(request.files['file']))
        filename = str(time()) + '_' + secure_filename(file.filename)
        tilted_filename = str(time()) + '_tilted_' + \
            secure_filename(file.filename)
        # time stamp plus filename
        destination = UPLOAD_FOLDER + '/' + filename
        file.save(destination)
        rotated_img = rotate_image(file)
        rotated_img.save(UPLOAD_FOLDER + '/' + tilted_filename)
        post = Post(image_url=url_for("download_file", filename=filename))
        db.session.add(post)
        post = Post(image_url=url_for(
            "download_file", filename=tilted_filename))
        db.session.add(post)
        db.session.commit()
        response = jsonify(
            {'status': 'OK', 'message': 'File uploaded successfully', 'filename': url_for("download_file", filename=filename)})
        response.status_code = 200
    except Exception as e:
        response = jsonify({'status': e})
        response.status_code = 500
    return response


@bp.route("/api/posts", methods=["GET"])
def get_posts():
    posts = Post.query.order_by(Post.created.desc()).all()
    return jsonify(posts=[post.serialize for post in posts])
