import os
from pydub import AudioSegment
import pydub


def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Export the audio to WAV format
    audio.export(wav_file, format="wav")


def convert_folder_mp3_to_wav(folder_path, max_files=20000):
    # Initialize a counter for the number of converted files
    converted_files_count = 0

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            mp3_file_path = os.path.join(folder_path, filename)
            # Construct the corresponding WAV file path
            wav_file_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".wav")

            # Specify the path to ffprobe explicitly
            # pydub.AudioSegment.converter = "E:\\personal files\\softwares\\ffmpeg-2024-01-28-git-e0da916b8f-full_build\\ffmpeg\\bin"  # Replace with the actual path to ffprobe
            pydub.AudioSegment.converter = "C:\\personal files\\Installation\\ffmpeg\\bin\\ffprobe.exe"
            pydub.AudioSegment.ffmpeg = "C:\\personal files\\Installation\\ffmpeg\\bin\\ffmpeg.exe"

            print("mp3_file_path:", mp3_file_path)
            print("wav_file_path:", wav_file_path)

            # Convert the MP3 file to WAV
            convert_mp3_to_wav(mp3_file_path, wav_file_path)
            print(f"Converted: {mp3_file_path} -> {wav_file_path}")

            # Increment the counter
            converted_files_count += 1

            # Check if the maximum number of files has been reached
            if converted_files_count >= max_files:
                break


def convert_all_folders(root_folder):
    # Iterate over all folders in the root folder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        # Check if it's a directory
        if os.path.isdir(folder_path):
            print(f"\nConverting files in folder: {folder_path}")
            convert_folder_mp3_to_wav(folder_path)


# Example usage:
root_folder = "E:\\personal files\\dataset\\archive_8\\Language Detection Dataset\\"
convert_all_folders(root_folder)
