from abc import abstractmethod, ABCMeta


class AbstractStack(metaclass=ABCMeta):
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def size(self):
        return self._size

    @property
    def top(self):
        return self.peek()

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass
