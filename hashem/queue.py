from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    """ Create a new queue that is empty """
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def size(self):
        """ Return the number of items in the queue """
        return self._size

    @property
    @abstractmethod
    def front(self):
        """ Return the front element of the queue """
        pass

    @property
    @abstractmethod
    def rear(self):
        """ Return the rear element of the queue """
        pass

    @abstractmethod
    def enqueue(self, item):
        """ Add a new item to the rear of the queue """
        pass

    @abstractmethod
    def dequeue(self):
        """ Remove the front item from the queue """
        pass

    @abstractmethod
    def clear(self):
        """ Remove all items from the queue """
        pass

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise """
        return self._size == 0


class QueueNode:
    """ Represents a single queue node """
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
