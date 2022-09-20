from datetime import datetime
from custom_time import CustomTime
from path import Path


class Subtitle:
    def __init__(self, video_path: str) -> None:
        self.subtitle_path = Path.change_extension(video_path, 'srt')
        self.subtitles = []

    def add_subtitle(self, start_time: datetime, end_time: datetime, subtitle: str) -> None:
        full_time = f'{CustomTime.to_string(start_time)} --> {CustomTime.to_string(end_time)}'
        self.subtitles.append(full_time)
        self.subtitles.append(f'{subtitle}\n')

    def save(self) -> None:
        with open(self.subtitle_path, 'w') as file:
            file.write('\n'.join(self.subtitles))

