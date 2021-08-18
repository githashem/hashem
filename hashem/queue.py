from abc import ABCMeta, abstractmethod


class AbstractQueue(metaclass=ABCMeta):
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def size(self):
        return self._size

    @abstractmethod
    @property
    def front(self):
        pass

    @abstractmethod
    @property
    def rear(self):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    def is_empty(self):
        return self._size == 0
