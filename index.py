from flask import Flask
from flask_cors import CORS
from routers.router import postMovieClip
UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)
# @app.route('/moveClip'
@app.route('/', methods=['GET'])
def helle():
    return '<h1>hello</h1>'
postMovieClip(app)
# def _moveClip():
if __name__ == '__main__':
    app.run(debug=False, port=8000, host='172.24.3.233')

