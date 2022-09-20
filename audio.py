import os
from moviepy.editor import AudioFileClip
from audio_wave import AudioWave
from path import Path


class Audio:
    def __init__(self, audio: AudioFileClip) -> None:
        self.audio = audio
        self.audio_path = Path.root_dir('.audio.wav')
        self.save_audio()
        self.audio_wave = AudioWave(self.audio_path)

    def save_audio(self) -> None:
        self.audio.write_audiofile(self.audio_path)

    def delete_audio(self) -> None:
        os.remove(self.audio_path)

        