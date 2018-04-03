import playlists
from ydl import ydl
import pyaudio
import wave

def loop ():
    playlist = playlists.ninety9lives

    with open('credits.txt', 'w') as f:
        f.write("These credits were created with Live Stream Music player by Clayton Does Things (https://github.com/ClaytonDoesThings/Live-Stream-Music-Player; https://www.youtube.com/channel/UChXdVQ8mm8UQBir87KaRgTQ?&ab_channel=ClaytonDoesThings)\n")

    while True:
        video = playlist.shuffle()
        print(video.title)
        with open('credits.txt', 'r+') as f:
            if video.credit not in f.read():
                f.write("\n" + video.credit + "\n")
        ydl({
            'file_name': 'audio',
            'codec': 'wav',
            'url': 'https://www.youtube.com/watch?v=' + video.id
        })
        play("audio.wav")
        

def play (file_name):
    print ("playing audio...")
    #define stream chunk   
    chunk = 1024  

    #open a wav format music
    f = wave.open(file_name, "rb")
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()
    print ("stopping audio...")