from abc import ABCMeta, abstractmethod
from collections.abc import Iterable


class DeadLinedMetaReminder(Iterable, ABCMeta):

    @abstractmethod
    def is_due(cls):
        pass