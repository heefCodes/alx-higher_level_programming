#!/usr/bin/python3
"""
Module 100-singly_linked_list
"""


class Node:
    """
    Class definition

    Args:
        data:
        next_node:
    """
    def __init__(self, data, next_node=None):
        """
        Initializes Node

        Args:
            data (_type_): _description_
            next_node (_type_, optional): _description_. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        A getter method

        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        A setter method

        Args:
            value (_type_): set data to value, if int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        A getter method

        Return: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
         A setter method

        Args:
            value (_type_): set next_node to value
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Class definition for SimglyLinkedList
    """
    def __init__(self):
        """
        Initializes singly linked list
        Attributes:
            head: private
        """
        self.__head = None

    def __str__(self):
        """
        String representation of singly linked list needed to print
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Inserts new nodes into singly linked list in sorted order
        Args:
        value: int data for node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
