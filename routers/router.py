import os
import json
from flask import request, jsonify
from werkzeug import secure_filename
from control.movieClip import movieClip
from control.unit import get_host_ip

def postMovieClip(app):
    @app.route('/postMovieClip', methods=['POST'])
    def route():
        info = json.loads(request.form['info'])
        if json.loads(request.form['isFastStart']):
            videoUrl = movieClip(mp4='1-06.mp4', img='startBG.jpeg', info=info)
        else:
            mp4File = request.files['mp4']
            imgFile = request.files['img']
            if mp4File:
                filename = secure_filename(mp4File.filename)
                mp4File.save(os.path.join(os.path.dirname(
                    __file__), './uploads', filename))
            if imgFile:
                filename = secure_filename(imgFile.filename)
                imgFile.save(os.path.join(os.path.dirname(
                    __file__), './uploads', filename))
            videoUrl = movieClip(mp4=mp4File.filename,
                                img=imgFile.filename, info=info)

        return jsonify({
            "videoUrl": str(get_host_ip()) + ':8000/static/product/' + videoUrl
        })
