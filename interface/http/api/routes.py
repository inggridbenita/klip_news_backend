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
