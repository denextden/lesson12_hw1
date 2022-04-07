from flask import Blueprint, render_template, request
from functions import load_posts
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    search_by_word = request.args['s']
    logging.info(f'Слово для поиска: {search_by_word}')
    posts = [x for x in load_posts() if search_by_word.lower() in x['content'].lower()]
    return render_template("post_list.html", search_by_word=search_by_word, posts=posts)
