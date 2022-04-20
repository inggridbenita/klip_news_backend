from flask import Flask, request
from flask_cors import CORS
import handler as h

app = Flask(__name__)
CORS(app)


@app.route('/get_all_news')
def get_all_news():
    return h.get_all_news()


if __name__ == "__main__":
    app.run(debug=True)
