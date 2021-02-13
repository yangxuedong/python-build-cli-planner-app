from abc import ABCMeta, abstractmethod
from collections.abc import Iterable


class DeadLinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass