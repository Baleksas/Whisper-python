import openai
import pyaudio
import wave


def record_voice():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    frames = []
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open("Recording.wav", "wb")

    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()


def get_voice():
    openai.api_key = "API-KEY"
    audio_file = open("Recording.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    record_voice()
    # get_voice()
