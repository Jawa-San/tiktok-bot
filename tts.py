from gtts import gTTS 
import os

directory = './tifu'

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename), "r") as f:
        data = f.read()  #.replace('\n', '')
        tts = gTTS(data)
        filename = filename[:-4]
        tts.save("./audio/" + filename + ".mp3")