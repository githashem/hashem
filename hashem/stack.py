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

    def is_empty(self):
        return self._size == 0


class StackNode:
    __slots__ = ['item', 'next']

    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedListStack(AbstractStack):
    def __init__(self):
        super().__init__()
        self._top = None

    def push(self, item):
        self._top = StackNode(item, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            item = self._top.item
            self._top = self._top.next
            self._size -= 1
            return item

    def peek(self):
        return self._top.item if self._top else None
