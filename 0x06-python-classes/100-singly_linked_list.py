#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Defines a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """INIT"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node
        
        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if type(value) is not Node and value is not None:
                raise TypeError("next_node must be a Node object")
            else:
                self.__data = value

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value)
        if (self.__head):
            current = self.__head
            if current.data > value:
                self.__head = Node(value, current)
            while (current.next.data < value):
                current = current.next
            if current.data < value:
                current.next = newNode
                if current.next.next:
                    newNode.next = current.next.next
            else:
                newNode.next = current
        else:
            self.__head = Node(value)

    def __str__(self):
        li = []
        current = self.head
        while current:
            li += current.data
            current = current.next
        return [node for node in li]
