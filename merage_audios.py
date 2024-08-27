""" pydub library """
import os
from pydub import AudioSegment

def merge_audio_files(first_audio_path, second_audio_path, output_directory, output_filename):
    # Load the audio files
    first_audio_segment = AudioSegment.from_file(first_audio_path)
    second_audio_segment = AudioSegment.from_file(second_audio_path)
    
    # Merge the audio files
    merged_audio = first_audio_segment + second_audio_segment
    
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Define the full path for the output file
    merged_filepath = os.path.join(output_directory, output_filename)
    
    # Save the merged audio file
    merged_audio.export(merged_filepath, format='wav')
    
    print(f"Merged audio saved to {merged_filepath}")
