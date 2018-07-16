from flask import Blueprint

posts = Blueprint('posts', __name__)


@posts.route("/posts/")
def get_all_posts():
    return "All posts"
