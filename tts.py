from gtts import gTTS 
import os
class Tts:
    def init(self, text):
        self.text = text
    #
    def tts(self, directory):
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), "r") as f:
                data = f.read()  #.replace('\n', '')
                self.tts = gTTS(data)
                filename = filename[:-4]
                self.tts.save("./audio/" + filename + ".mp3")