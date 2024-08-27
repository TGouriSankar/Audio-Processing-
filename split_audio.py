""" pydub library """

import os
from pydub import AudioSegment

def split_audio_into_chunks(audio_path, chunk_length_sec=10, output_directory=None):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)
    
    # Calculate the total length of the audio in milliseconds
    audio_length_ms = len(audio)
    chunk_length_ms = chunk_length_sec * 1000  # Convert seconds to milliseconds
    
    # Determine the output directory
    if output_directory is None:
        output_directory = os.path.dirname(audio_path)
    
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Split the audio into chunks
    for i in range(0, audio_length_ms, chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_filename = f"chunk_{i // chunk_length_ms + 1}.wav"
        chunk_filepath = os.path.join(output_directory, chunk_filename)
        chunk.export(chunk_filepath, format='wav')
        print(f"Saved {chunk_filepath}")
