import unittest
from hashem.stack import LinkedListStack


class LinkedListStackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = LinkedListStack()

    def test_size(self):
        self.assertEqual(self.stack.size, 0, "when instance is made, size must be 0")
        self.stack.push('item 1')
        self.assertEqual(self.stack.size, 1, "when a item is pushed, size must be 1")
        self.stack.multi_push(range(10))
        self.assertEqual(self.stack.size, 11)
        self.stack.multi_pop(10)
        self.assertEqual(self.stack.size, 1)
        self.stack.pop()
        self.assertEqual(self.stack.size, 0, "when a item is poped, size must be 0")
        self.stack.pop()
        self.assertEqual(self.stack.size, 0, "when stack is empty, size must be 0")

    def test_top(self):
        self.assertIsNone(self.stack.top, "when instance is made, top must be none")
        self.stack.push('item 1')
        self.assertEqual(self.stack.top, 'item 1', "when a item is pushed, top must be that item")
        self.stack.push('item 2')
        self.stack.pop()
        self.assertEqual(self.stack.top, 'item 1', "when a item is poped, top must be before that item")
        self.stack.pop()
        self.assertIsNone(self.stack.top, "when stack is empty, top must be none")

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty(), "when instance is made, stack must be empty")
        self.stack.push('item 1')
        self.assertFalse(self.stack.is_empty(), "when stack is pushed, stack mustn't be empty")
        self.stack.push('item 2')
        self.stack.pop()
        self.assertFalse(self.stack.is_empty(), "when items are in stack, stack mustn't be empty")
        self.stack.pop()
        self.assertTrue(self.stack.is_empty(), "when items aren't in stack, stack must be empty")





