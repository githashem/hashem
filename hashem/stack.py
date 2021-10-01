from abc import ABC, abstractmethod

__all__ = ['AbstractStack', 'LinkedListStack', 'StackNode']


class AbstractStack(ABC):
    """ Create a new stack that is empty """
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"Stack({repr(self.top)})"

    @property
    def size(self):
        """ Return the number of items on the stack """
        return self._size

    @property
    def top(self):
        """ Return the top item from the stack """
        return self.peek()

    @abstractmethod
    def push(self, item):
        """ Add a item to the top of the stack """
        pass

    @abstractmethod
    def pop(self):
        """ Remove the top item from the stack """
        pass

    @abstractmethod
    def peek(self):
        """ Return the top item from the stack but does not remove it """
        pass

    @abstractmethod
    def clear(self):
        """ Remove all items from the stack """
        pass

    def is_empty(self):
        """ Return True if the stack is empty, False otherwise """
        return self._size == 0

    def multi_push(self, iterable):
        for item in iterable:
            self.push(item)

    def multi_pop(self, number):
        for _ in range(number):
            self.pop()


class StackNode:
    """ Represents a single stack node """
    __slots__ = ['item', 'next']

    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return repr(self.item)


class LinkedListStack(AbstractStack):
    def __init__(self):
        super().__init__()
        self._head = None

    def __iter__(self):
        node = self._head
        while node:
            yield node.item
            node = node.next

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
