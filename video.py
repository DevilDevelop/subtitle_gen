from datetime import datetime, timedelta
from moviepy.editor import VideoFileClip
from audio import Audio
from subtitle import Subtitle
from recognizer import Recognizer
from translator import Translator
import os


class Video:
    def __init__(self, file_path: str, video_language: str, translate_language: str) -> None:
        self.file_path = file_path
        self.video_language = video_language
        self.translate_language = translate_language
        self.video_obj = VideoFileClip(self.file_path)
        self.audio = Audio(self.video_obj.audio)
        self.subtitles = Subtitle(self.file_path)

    def create_subtitles(self) -> None:
        start_time = datetime(year=1, month=1, day=1)
        for index, chunk in enumerate(self.audio.audio_wave.audio_chunks):
            progress = (index / len(self.audio.audio_wave.audio_chunks)) * 100
            end_time = start_time + timedelta(milliseconds=len(chunk))
            chunk.export(self.audio.audio_path, format='wav')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Progress: {round(progress, 2)}')
            try:
                if self.translate_language:
                    text = Recognizer.transcribe(self.audio.audio_path, self.video_language)
                    subtitle = Translator.translate(text, self.video_language, self.translate_language)
                    
                else:
                    subtitle = Recognizer.transcribe(self.audio.audio_path, self.video_language)

                self.subtitles.add_subtitle(start_time, end_time, subtitle)
                start_time = end_time

            except Exception as e:
                print(e)

            finally:
                self.audio.delete_audio()
                
        self.subtitles.save()
        
