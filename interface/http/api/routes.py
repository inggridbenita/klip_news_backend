from flask import request, Blueprint
from interface.http.api import handler as h

routes = Blueprint('routes', __name__)


@routes.route('/get_all_news')
def get_all_news():
    return h.get_all_news_handler()


@routes.route('/get_news_detail')
def get_news_detail():
    news_id = request.args.get('id')
    return h.get_news_detail_handler(news_id)


@routes.route('/get_arr_news_detail', methods=['POST', 'GET'])
def get_arr_news_detail():
    body = request.json
    return h.get_arr_news_detail_handler(body)


@routes.route('/get_news_by_category', methods=['POST', 'GET'])
def get_news_by_category():
    args = request.args
    return h.get_news_by_category_handler(args.get("category", default="", type=str))


@routes.route('/get_recommendation', methods=['POST', 'GET'])
def get_recommendation():
    body = request.json
    return h.get_recommendation_handler(body)
