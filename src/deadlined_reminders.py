from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil import parser
from datetime import datetime


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC, Iterable):

    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):

    def __init__(self, text, date):
        self.date = parser(date, dayfirst=True)
        self.text = text

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        formatted_date = self.date.isoformat()
        return iter([text, formatted_date])