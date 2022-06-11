from __main__ import app
from __main__ import request
from __main__ import h


@app.route('/get_all_news')
def get_all_news():
    return h.get_all_news_handler()


@app.route('/get_news_detail')
def get_news_detail():
    news_id = request.args.get('id')
    return h.get_news_detail_handler(news_id)
