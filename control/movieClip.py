
import os
from moviepy.editor import *
from moviepy.video.tools.drawing import circle
from moviepy.video.tools.drawing import color_split
import time

def movieClip(*, mp4, img, info):
    img = ImageSequenceClip(
        [rootPath('../uploads/' + img)], fps=.5).subclip(0, 20)
    w = img.size[0]
    h = img.size[1]
    y = info['position']['top'] * (w / 500)
    x = info['position']['left'] * (w / 500)
    vW = info['size']['width'] * (w / 500)
    vH = info['size']['height'] * (w / 500)
    print(x,y)

    img = img.resize((w, h))
    clip = (VideoFileClip(rootPath('../uploads/'+mp4), audio=True)
            .subclip(0, 20).
            resize((vW, vH)).    # one third of the total screen
            set_position((x, y))
            )
    video = CompositeVideoClip([img, clip])
    newFileName = str(time.time())+ '.avi' 
    video.write_videofile(
        rootPath('../static/product/%s' % (newFileName)), codec = 'libx264',fps= 30)
    return newFileName


def rootPath(path):
    return os.path.join(os.path.dirname(__file__), path)
