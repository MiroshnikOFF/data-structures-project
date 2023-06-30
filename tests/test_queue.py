"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Node, Queue
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
        node = Node(data)
        self.assertEqual(node.next_node, None)


class TestQueue(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        queue.head = 10
        queue.tail = 20
        self.assertEqual(queue.head, 10)
        self.assertEqual(queue.tail, 20)

    def test_enqueue(self):
        queue = Queue()
        data_1 = 1
        data_2 = 2
        data_3 = 3
        queue.enqueue(data_1)
        self.assertEqual(queue.head.data, data_1)
        self.assertEqual(queue.head.next_node, None)
        queue.enqueue(data_2)
        self.assertEqual(queue.head.data, data_1)
        self.assertEqual(queue.head.next_node.data, data_2)
        queue.enqueue(data_3)
        self.assertEqual(queue.head.data, data_1)
        self.assertEqual(queue.head.next_node.data, data_2)
        self.assertEqual(queue.head.next_node.next_node.data, data_3)

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), "")
        queue.enqueue("data_1")
        queue.enqueue("data_2")
        queue.enqueue("data_3")
        self.assertEqual(str(queue), "data_1\ndata_2\ndata_3")

