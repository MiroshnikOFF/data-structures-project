class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, None)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if not self.top:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next_node
        return data

    def __str__(self):
        if self.top:
            current = self.top
            stack_str = ""
            while current:
                stack_str += str(current.data) + "\n"
                current = current.next_node
            return stack_str
        else:
            return "Стек пуст"

