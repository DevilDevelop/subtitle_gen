from abc import abstractmethod
from datetime import datetime


class CustomTime:

    @abstractmethod    
    def to_string(date: datetime) -> str:
        format_string = r'%H:%M:%S,%f'
        date_string = date.strftime(format_string)
        return date_string[:-3]

    @abstractmethod
    def to_millisecond(date: datetime) -> int:
        return int((date.second * 1000) + (date.microsecond / 1000))

