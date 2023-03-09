import os
import openai
import keyboard
import pyaudio
import wave
import datetime
import pyttsx3

openai.api_key = os.getenv("OPENAI_API_KEY")

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()

is_recording = False
frames = []

def start_recording():
    global is_recording, frames
    is_recording = True
    frames = []
    print("Listening...")

def stop_recording():
    global is_recording
    is_recording = False
    print("Thinking...")
    save_recording()

# Submit a prompt to OpenAI and get its response
def Submit_Prompt(Prompt:str)->str:
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = Prompt,
        temperature = 0.3,
        max_tokens = 4000,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    return response.choices[0].text;

def ThinkAndRespond(filename:str):
    audio_file= open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print("> HUMAN SCUM: "+transcript.text)
    killbot9000_wisdom = Submit_Prompt(Prompt=transcript.text)
    print("> KILLBOT 9000: "+str.strip(killbot9000_wisdom))
    speak(killbot9000_wisdom)

def save_recording():
    global frames
    now = datetime.datetime.now()
    file_name = now.strftime("%Y%m%d%H%M%S") + ".wav"
    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    ThinkAndRespond(filename=file_name)

def callback(in_data, frame_count, time_info, status):
    global frames
    if is_recording:
        frames.append(in_data)
    return (in_data, pyaudio.paContinue)

def speak(word:str):
    # Create the engine
    engine = pyttsx3.init()
    # Set the properties for the engine
    engine.setProperty('rate', 150)    # Speed of speaking
    engine.setProperty('volume', 1.0)  # Volume of speaking
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    #engine.setProperty('voice', 'english-us')  # Voice to use for speaking
    # Speak the word in a robotic voice
    engine.say(word)
    engine.runAndWait()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

stream.stop_stream()

while True:
    event = keyboard.read_event()
    if event.event_type == "down":
        if event.name == "r":
            if not is_recording:
                start_recording()
                stream.start_stream()
            else:
                stop_recording()
                stream.stop_stream()
        elif event.name == "q":
            if is_recording:
                stop_recording()
                stream.stop_stream()
            break

stream.close()
audio.terminate()
