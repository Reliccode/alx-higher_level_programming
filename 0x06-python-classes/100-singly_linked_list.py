#!/usr/bin/python3
"""
Module - Singly Linked List
"""


class Node:
    """
    Class defining node of singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a node

        Args:
            data: int data value of the node
            next_node (Node): next node in list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute

        Returns:
            int: data value of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data attribute

        Args:
            value (int): int data value to set

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node attribute

        Returns:
            Node: next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for next_node attribute

        Args:
            value (Node): next node to set

        Raises:
            TypeError: If value is not a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class defining singly linked list
    """
    def __init__(self):
        """
        Initializes empty singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts new Node to correct sorted position in list (increasing order)

        Args:
            value: int value of the new Node
        """
        new_node = Node(value)

        if self.head is None:
            # List is empty, new node is now head
            self.head = new_node
        elif value < self.head.data:
            # New node be inserted at beginning
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns string representation of e linked list

        Returns:
            str: string representation of linked list
        """
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
