# -*- coding: utf-8 -*-


class DoublyLinkedNode:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # converts LinkedList to Python list with nodes values as elements
    def to_values_list(self):
        result = []
        node = self.head

        while node is not None:
            result.append(node.value)
            node = node.next

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
    def remove_by_value(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                if node.prev is None:
                    self.head = node.next
                    self.head.prev = None
                elif node.next is None:
                    self.tail = node.prev
                    self.tail.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev

                del node
                return

            node = node.next

    # inserting node after target node
    def insert_after(self, new_node, target_node):
        if target_node is None:
            return

        node = self.head
        while node is not None:
            if node == target_node:
                # setting scheme: [ node <-> new_node <-> node.next ]

                if node.next is None:
                    self.tail = new_node        # in tail case move tail-pointer
                else:
                    node.next.prev = new_node   # previous node for next node will be new node

                new_node.next = node.next   # after new node will go next node
                new_node.prev = node        # current node will be before new node
                node.next = new_node        # after current node will go new node

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
