"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import Node, LinkedList
import unittest

if __name__ == '__maie__':
    unittest.main()


class TestNode(unittest.TestCase):

    def test_init(self):
        data = "test"
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertEqual(node.next_node, None)


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        ll.head = 10
        self.assertEqual(ll.head, 10)

    def test_str(self):
        ll = LinkedList()
        ll.insert_beginning({'test': 'ok'})
        self.assertEqual(str(ll), "{'test': 'ok'} -> None")

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 3})
        self.assertEqual(str(ll), "{'id': 3} -> None")
        ll.insert_beginning({'id': 2})
        self.assertEqual(str(ll), "{'id': 2} -> {'id': 3} -> None")
        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 3})
        self.assertEqual(str(ll), "{'id': 3} -> None")
        ll.insert_at_end({'id': 2})
        self.assertEqual(str(ll), "{'id': 3} -> {'id': 2} -> None")
        ll.insert_at_end({'id': 1})
        self.assertEqual(str(ll), "{'id': 3} -> {'id': 2} -> {'id': 1} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}])
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.assertEqual(ll.to_list(), [
            {'id': 1, 'username': 'lazzy508509'},
            {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}])
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.to_list(), [
            {'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
            {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(0), {'id': 0, 'username': 'serebro'})

    def test_exception_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertRaises(TypeError, ll.get_data_by_id(2))


