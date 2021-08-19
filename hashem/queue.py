from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def size(self):
        return self._size

    @property
    @abstractmethod
    def front(self):
        pass

    @property
    @abstractmethod
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


class QueueNode:
    __slots__ = ['item', 'next']

    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedListQueue(AbstractQueue):
    def __init__(self):
        super().__init__()
        self._front = None
        self._rear = None

    def enqueue(self, item):
        if self.is_empty():
            self._front = self._rear = QueueNode(item)
        else:
            self._rear.next = self._rear = QueueNode(item)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            item = self._front.item
            self._front = self._front.next
            self._size -= 1
            return item

    def clear(self):
        self._size = 0
        self._front = None
        self._rear = None

    def front(self):
        return self._front.item

    def rear(self):
        return self._rear.item
