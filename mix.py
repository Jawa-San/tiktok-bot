import os
from moviepy.editor import *
from moviepy.video.fx.all import *

clip = VideoFileClip("clip.mp4")
audioclip = AudioFileClip("./audio/anniversary.mp3")
audio = audioclip.subclip(0,10)
videoclip = clip.set_audio(audio)
videoclip.write_videofile("clip2.mp4")