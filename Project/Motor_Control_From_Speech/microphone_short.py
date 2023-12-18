import wave
import sys
import math
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1

RATE = 44100
RECORD_SECONDS = 0.5

def record():
    wf = wave.open('left.wav', 'wb')
    wf2 = wave.open('right.wav', 'wb')
    

    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    stream = p.open(input_device_index=2, format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
    print('Recording...')
    
    p2 = pyaudio.PyAudio()
    wf2.setnchannels(CHANNELS)
    wf2.setsampwidth(p2.get_sample_size(FORMAT))
    wf2.setframerate(RATE)
    stream2 = p2.open(input_device_index=4, format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
    print('Recording...')

    for _ in range(0, math.ceil(RATE // CHUNK * RECORD_SECONDS)):
        wf.writeframes(stream.read(CHUNK))
        wf2.writeframes(stream2.read(CHUNK))
    print('Done')
    stream.close()
    stream2.close()
    p.terminate()
    p2.terminate()
