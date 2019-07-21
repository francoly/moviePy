from flask import Flask
from flask_cors import CORS
# from routers.router import postMovieClip
UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def helle():
    return '<h1>hello</h1>'
# @app.route('/moveClip'
# postMovieClip(app)
# def _moveClip():
if __name__ == '__main__':
    app.run(debug=False,port=8000)
