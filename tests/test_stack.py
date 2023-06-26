"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Node, Stack

@pytest.mark.parametrize("data, next_node", [(5, "a"), (None, 8), ("D", 0.4), (None, None), (13, 88)])
def test_node_init(data, next_node):
    expected_data = data
    expected_new_node = next_node
    node = Node(data, next_node)
    assert node.data == expected_data
    assert node.next_node == expected_new_node


def test_stack_init():
    stack = Stack()
    assert stack.top == None


@pytest.mark.parametrize("data, expected", [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), ])
def test_push(data, expected):
    stack = Stack()
    new_node = Node(data, None)
    new_node.next_node = stack.top
    stack.top = new_node
    assert stack.top.data == expected
