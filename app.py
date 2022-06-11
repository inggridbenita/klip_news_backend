from flask import Flask, request
from flask_cors import CORS
import handler as h

app = Flask(__name__)
CORS(app)


if __name__ == "__main__":
    app.run(debug=True)
