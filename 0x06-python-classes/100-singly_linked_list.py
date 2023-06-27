#!/usr/bin/python3
"""
"Single Linked List" module.
This module initializes a default head of None.
The module has class Node that takes in integer values as data
within each node
"""


class Node:
    """A class that represents a single Node in a Linked List."""

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.next_node = next_node


class SinglyLinkedList:
    """A class that represents a Singly Linked List."""

    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        representation = ""
        while current:
            representation += str(current.data)
            current = current.next_node
            if current:
                representation += "\n"
        return representation

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
