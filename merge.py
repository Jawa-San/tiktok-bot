import os
from moviepy.editor import *
from moviepy.video.fx.all import *
from main import makeDirectory
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1/bin/ffmpeg"

clip = VideoFileClip("./gameplay/test.mp4")
clip = clip.resize((1080,1920))
# audio = AudioFileClip("./audio/anniversary.mp3")
# clip = clip.subclip(0, audio.duration)
# videoclip = clip.set_audio(audio)
# videoclip.write_videofile("clip.mp4")

directory = './audio'
makeDirectory("merged")

x = 0
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), "r") as f:
        audio = AudioFileClip(f.name)
        clip = clip.subclip(0, audio.duration)
        videoclip = clip.set_audio(audio)
        x += 1
        videoclip.write_videofile(f"./merged/clip{x}.mp4")