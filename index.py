from flask import Flask
from flask_cors import CORS
from routers.router import postMovieClip
UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)
# @app.route('/moveClip'
postMovieClip(app)
# def _moveClip():
if __name__ == '__main__':
    app.run(debug=True, port=8000)
