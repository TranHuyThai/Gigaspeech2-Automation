import os
import wave
import contextlib

def get_total_wav_duration(directory):
    total_duration = 0.0

    for filename in os.listdir(directory):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(directory, filename)
            with contextlib.closing(wave.open(filepath, 'r')) as wav_file:
                frames = wav_file.getnframes()
                rate = wav_file.getframerate()
                duration = frames / float(rate)
                total_duration += duration

    return total_duration

# Set the directory to the current folder (or specify another folder)
directory = "/home/stud_thai/project/audio_collection/GigaSpeech2/pipeline/convert_transcribe/output_trans/Entertainment/jianhao/audios"
total_duration = get_total_wav_duration(directory)

# Print result in minutes & seconds
minutes = int(total_duration // 60)
seconds = int(total_duration % 60)
print(f"Total duration: {minutes} min {seconds} sec ({total_duration:.2f} seconds)")
