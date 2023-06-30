"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack
import unittest

if __name__ == '__maie__':
    unittest.main()


class TestNode(unittest.TestCase):

    def test_init(self):
        data = "test"
        next_node = 10
        node = Node(data, next_node)
        self.assertEqual(node.data, data)
        self.assertEqual(node.next_node, next_node)


class TestStack(unittest.TestCase):

    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.top = 10
        self.assertEqual(stack.top, 10)

    def test_str(self):
        stack = Stack()
        self.assertEqual(str(stack), "Стек пуст")
        stack.push("data_1")
        stack.push("data_2")
        stack.push("data_3")
        self.assertEqual(str(stack), "data_3\ndata_2\ndata_1\n")

    def test_push(self):
        stack = Stack()
        data_1 = 1
        data_2 = 2
        data_3 = 3
        stack.push(data_1)
        self.assertEqual(stack.top.data, data_1)
        self.assertEqual(stack.top.next_node, None)
        stack.push(data_2)
        self.assertEqual(stack.top.data, data_2)
        self.assertEqual(stack.top.next_node.data, data_1)
        stack.push(data_3)
        self.assertEqual(stack.top.data, data_3)
        self.assertEqual(stack.top.next_node.data, data_2)
        self.assertEqual(stack.top.next_node.next_node.data, data_1)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(data, 'data3')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')
        data = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(data, 'data1')
