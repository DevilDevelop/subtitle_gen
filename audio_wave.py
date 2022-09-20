from pydub import AudioSegment
from pydub.silence import split_on_silence


class AudioWave:
    def __init__(self, audio_path: str) -> None:
        self.audio = AudioSegment.from_wav(audio_path)
        self.audio_chunks = split_on_silence(
            audio_segment=self.audio,
            min_silence_len=500,
            silence_thresh=-40,
            keep_silence=500
        )

