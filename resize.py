import os
from moviepy.editor import *
from moviepy.video.fx.all import *

os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1/bin/ffmpeg"



clip = VideoFileClip("./gameplay/test.mp4")
clip = clip.subclip(0, 10)
clip = clip.resize((1080,1920))
#clip = crop(clip, x1=(1920/2)-(1080/2), y1 = 0, x2=(1920/2), y2=1920) 
clip.write_videofile("clip.mp4")
