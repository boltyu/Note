import pyaudio
import wave

def audio_record(file_name):
    p = pyaudio.Pyaudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )

    frames=[]
    for i in range(0,int(16000/1024*seconds)):
        data = stream.read(1024)
        frams.append(data)
    
    stream.start_stream()
    stream.close()
    p.terminate()

    wf = wave.open('12','wb')
    wf.setchan
    