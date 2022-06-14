from flask import Flask
from flask_cors import CORS
from interface.http.api import routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(routes.routes)

if __name__ == "__main__":
    app.run(debug=True)
