from gtts import gTTS 

with open('tifu/Tifu by eating my husbands anniversary breakfast he made me.txt', 'r') as file:
    data = file.read().replace('\n', '')


tts = gTTS(data)
print(type(data))
tts.save("./audio/hello.mp3")