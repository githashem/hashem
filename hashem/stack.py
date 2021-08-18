from abc import abstractmethod, ABCMeta

__all__ = ['AbstractStack', 'LinkedListStack', 'StackNode']


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

    @abstractmethod
    def clear(self):
        pass

    def is_empty(self):
        return self._size == 0

    def multi_push(self, iterable):
        for item in iterable:
            self.push(item)

    def multi_pop(self, number):
        for _ in range(number):
            self.pop()


class StackNode:
    __slots__ = ['item', 'next']

    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedListStack(AbstractStack):
    def __init__(self):
        super().__init__()
        self._head = None

    def push(self, item):
        self._head = StackNode(item, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            item = self._head.item
            self._head = self._head.next
            self._size -= 1
            return item

    def peek(self):
        return self._head.item if self._head else None

    def clear(self):
        self._size = 0
        self._head = None
