# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self, init_list=[]):
        self.head = None
        self.tail = None

        for node in init_list:
            self.add_in_tail(Node(node))

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def to_values_list(self, reversed=False):
        """
        Converts LinkedList to Python list with nodes values as elements
        :param reversed: when stands True makes reversed list (starts from end)
        :return: list of node values
        """
        result = []

        if not reversed:
            node = self.head
            while node is not None:
                result.append(node.value)
                node = node.next
        else:
            node = self.tail
            while node is not None:
                result.append(node.value)
                node = node.prev

        return result

    # getter i-element
    def get(self, index):
        i = 0
        node = self.head

        while node is not None:
            if index == i:
                return node

            i += 1
            node = node.next

        return None

    # removing first-founded node by value
    def delete(self, value, all=False):
        node = self.head
        while node is not None:
            if node.value == value:
                """
                If deleted node is head:
                    * move head ptr to next
                    * update ptr of head prev element as None
                """
                if node == self.head:
                    self.head = self.head.next
                    # Head can stands None (single-element-list-case), so checking it
                    if self.head is not None:
                        self.head.prev = None

                """
                If deleted node is tail:
                    * move tail ptr  to prev
                    * update ptr of tail next element as None
                """
                if node == self.tail:
                    self.tail = node.prev
                    # Tail can stands None (single-element-list-case), so checking it
                    if self.tail is not None:
                        self.tail.next = None

                """ Update other ptrs """
                if node.prev is not None:
                    node.prev.next = node.next
                if node.next is not None:
                    node.next.prev = node.prev

                """
                Saving pointer for deleting
                and moving pointer to the next element
                """
                node_pointer = node
                node = node.next
                del node_pointer

                if not all:
                    return
            else:
                node = node.next

    # inserting node after target node
    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)

        node = self.head
        while node is not None:
            if node == afterNode:
                # setting scheme: [ node <-> new_node <-> node.next ]
                newNode.next = node.next   # after new node will go next node
                newNode.prev = node        # current node will be before new node
                node.next = newNode        # after current node will go new node

                # Update tail pointer if required
                if node == self.tail:
                    self.tail = newNode
                else:
                    newNode.next.prev = newNode   # previous node for next node will be new node

                return

            node = node.next

    # adding new node to head
    def add_in_head(self, item):
        if self.head is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            item.next = self.head
            self.head.prev = item
            item.prev = None
        self.head = item

    def find(self, val):
        return self._find(val, all=False)

    def find_all(self, val):
        return self._find(val, all=True)

    def clean(self):
        """
        Clear list.
        Moving through each node and set its pointers as None
        """
        node = self.head
        while node is not None:
            next_node = node.next
            node.prev = None
            node.next = None
            node = next_node
        self.head = None
        self.tail = None

    def len(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next

        return counter

    def _find(self, val, all):
        """
        Inner function for searching, can return both first entry and list of entries
        :param val: searched value
        :param all: stands true if requested to return list of entries
        :return: first entry if f_all is false, or list of entries if f_all is true
        """
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                if all:
                    result.append(node)
                else:
                    return node
            node = node.next

        if all:
            return []
        else:
            return None
