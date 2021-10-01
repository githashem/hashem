import unittest
from hashem.stack import LinkedListStack


class LinkedListStackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = LinkedListStack()

    def test_size(self):
        self.assertEqual(self.stack.size, 0)
        self.stack.push('item 1')
        self.assertEqual(self.stack.size, 1)
        self.stack.multi_push(range(10))
        self.assertEqual(self.stack.size, 11)
        self.stack.multi_pop(10)
        self.assertEqual(self.stack.size, 1)
        self.stack.pop()
        self.assertEqual(self.stack.size, 0)
        self.stack.pop()
        self.assertEqual(self.stack.size, 0)

    def test_top(self):
        self.assertIsNone(self.stack.top)
        self.stack.push('item 1')
        self.assertEqual(self.stack.top, 'item 1')
        self.stack.push('item 2')
        self.stack.pop()
        self.assertEqual(self.stack.top, 'item 1')
        self.stack.pop()
        self.assertIsNone(self.stack.top)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push('item 1')
        self.assertFalse(self.stack.is_empty())
        self.stack.push('item 2')
        self.stack.pop()
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
