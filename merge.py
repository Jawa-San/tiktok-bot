import os
from moviepy.editor import *
from moviepy.video.fx.all import *
from main import makeDirectory
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1/bin/ffmpeg"
class Video:
    def init(self, video):
        self.video = VideoFileClip(video)

    def merge(self, directory):
        count = 0
        self.video = self.video.resize((1080,1920))
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), "r") as f:
                name = AudioFileClip(f.name)
                self.video = self.video.subclip(0, name.duration)
                self.video = self.video.set_audio(name)
                count += 1
                self.video.write_videofile(f"./merged/clip{count}.mp4")
# directory = './audio'
# makeDirectory("merged")

# x = 0
# for filename in os.listdir(directory):
#     with open(os.path.join(directory, filename), "r") as f:
#         audio = AudioFileClip(f.name)
#         clip = clip.subclip(0, audio.duration)
#         videoclip = clip.set_audio(audio)
#         x += 1
#         videoclip.write_videofile(f"./merged/clip{x}.mp4")