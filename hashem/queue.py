from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    """ Create a new queue that is empty """
    def __init__(self):
        self._size = 0
        self._front = None
        self._rear = None

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"Queue({repr(self.front)})"

    @property
    def size(self):
        """ Return the number of items in the queue """
        return self._size

    @property
    def front(self):
        """ Return the front element of the queue """
        if self.is_empty():
            return None
        return self._front.item

    @property
    def rear(self):
        """ Return the rear element of the queue """
        if self.is_empty():
            return None
        return self._rear.item

    @abstractmethod
    def enqueue(self, item):
        """ Add a new item to the rear of the queue """
        pass

    @abstractmethod
    def dequeue(self):
        """ Remove the front item from the queue """
        pass

    def clear(self):
        """ Remove all items from the queue """
        self._size = 0
        self._front = None
        self._rear = None

    def is_empty(self):
        """ Return True if the queue is empty, False otherwise """
        return self._size == 0 and self._front is None and self._rear is None


class QueueNode:
    """ Represents a single queue node """
    __slots__ = ['item', 'next']

    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return repr(self.item)


class LinkedListQueue(AbstractQueue):
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
