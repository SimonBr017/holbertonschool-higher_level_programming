#!/usr/bin/python3
"""class Node that defines a node of a singly linked list """


class Node:
    """class with attribute"""
    __next_node = None
    __data = 0

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(self.data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or type(self.__next_node) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        head = self.__head
        result = ""

        while (head is not None):
            result += str(head.data)
            if (head.next_node is not None):
                result += "\n"
            head = head.next_node
        return result

    def sorted_insert(self, value):
        new = Node(value)
        head = self.__head

        while head is not None and head.next_node is not None and \
                head.next_node.data < new.data:
            head = head.next_node

        if head is None:
            self.__head = new
        else:
            new.next_node = head.next_node
            head.next_node = new
            if (head.data > new.data):
                tmp = new.data
                new.data = head.data
                head.data = tmp
