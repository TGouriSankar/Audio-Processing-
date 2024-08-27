""" Short & Best way from librosa """
import librosa
audio, sr = librosa.load("path/to/your/file.wav", sr=None)
duration_in_seconds = librosa.get_duration(y=audio, sr=sr)


""" use the wave module along with contextlib for cleaner resource management """
import wave
import contextlib

def get_wav_duration(file_path):
    with contextlib.closing(wave.open(file_path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

# Example usage:
wav_file = "path/to/your/file.wav"
duration_in_seconds = get_wav_duration(wav_file)
print(f"WAV file duration: {duration_in_seconds} seconds")


""" librosa library """
import librosa

def get_wav_duration(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    duration = librosa.get_duration(y=audio, sr=sr)
    return duration

# Example usage:
wav_file = "path/to/your/file.wav"
duration_in_seconds = get_wav_duration(wav_file)
print(f"WAV file duration: {duration_in_seconds} seconds")


""" only wave library """
import wave

def get_wav_duration(file_path):
    with wave.open(file_path, 'r') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

# Example usage:
wav_file = "path/to/your/file.wav"
duration_in_seconds = get_wav_duration(wav_file)
print(f"WAV file duration: {duration_in_seconds} seconds")

""" pydub library """
from pydub import AudioSegment

def get_wav_duration(file_path):
    audio = AudioSegment.from_wav(file_path)
    duration = len(audio) / 1000.0  # Duration in seconds
    return duration

# Example usage:
wav_file = "path/to/your/file.wav"
duration_in_seconds = get_wav_duration(wav_file)
print(f"WAV file duration: {duration_in_seconds} seconds")
