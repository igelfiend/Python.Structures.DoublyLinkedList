# -*- coding: utf-8 -*-


import unittest
from main import *


def prepare_list():
    result = DoublyLinkedList()
    result.add_in_tail(DoublyLinkedNode(32))
    result.add_in_tail(DoublyLinkedNode(42))
    result.add_in_tail(DoublyLinkedNode(12))
    result.add_in_tail(DoublyLinkedNode(45))
    result.add_in_tail(DoublyLinkedNode(47))
    result.add_in_tail(DoublyLinkedNode(49))
    result.add_in_tail(DoublyLinkedNode(24))
    result.add_in_tail(DoublyLinkedNode(32))
    result.add_in_tail(DoublyLinkedNode(11))
    result.add_in_tail(DoublyLinkedNode(55))

    return result


class MyTestCase(unittest.TestCase):
    def test_remove_by_value(self):
        test_list = prepare_list()
        test_list.remove_by_value(12)
        self.assertEqual(test_list.to_values_list(), [32, 42, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'remove_by_value'. Normal case.")

    def test_remove_by_value_head_element(self):
        test_list = prepare_list()
        test_list.remove_by_value(32)
        self.assertEqual(test_list.to_values_list(), [42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'remove_by_value'. Head element case.")

    def test_remove_by_value_tail_element(self):
        test_list = prepare_list()
        test_list.remove_by_value(55)
        self.assertEqual(test_list.to_values_list(), [32, 42, 12, 45, 47, 49, 24, 32, 11],
                         "Testing: 'remove_by_value'. Tail element case.")

    def test_remove_by_value_from_empty_list(self):
        test_list = DoublyLinkedList()
        test_list.remove_by_value(55)
        self.assertEqual(test_list.to_values_list(), [],
                         "Testing: 'remove_by_value'. Empty list case.")

    def test_remove_by_value_which_not_present(self):
        test_list = prepare_list()
        test_list.remove_by_value(66)
        self.assertEqual(test_list.to_values_list(), [32, 42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'remove_by_value'. Element not present case.")

    # ----------------------------------------------------------------------------------------------

    def test_insert_after(self):
        test_list = prepare_list()
        test_list.insert_after(DoublyLinkedNode(50), test_list.get(3))
        self.assertEqual(test_list.to_values_list(), [32, 42, 12, 45, 50, 47, 49, 24, 32, 11, 55],
                         "Testing: 'insert_after'. Inserting in middle of list.")

    def test_insert_after_head(self):
        test_list = prepare_list()
        test_list.insert_after(DoublyLinkedNode(50), test_list.get(0))
        self.assertEqual(test_list.to_values_list(), [32, 50, 42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'insert_after'. Inserting after head element of list.")

    def test_insert_after_tail(self):
        test_list = prepare_list()
        test_list.insert_after(DoublyLinkedNode(50), test_list.get(9))
        self.assertEqual(test_list.to_values_list(), [32, 42, 12, 45, 47, 49, 24, 32, 11, 55, 50],
                         "Testing: 'insert_after'. Inserting after tail element of list.")

    def test_insert_after_none_element(self):
        test_list = prepare_list()
        test_list.insert_after(DoublyLinkedNode(50), test_list.get(10))
        self.assertEqual(test_list.to_values_list(), [32, 42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'insert_after'. Inserting after none element of list.")

    def test_insert_after_element_not_from_list(self):
        test_list = prepare_list()
        test_list.insert_after(DoublyLinkedNode(50), DoublyLinkedNode(10))
        self.assertEqual(test_list.to_values_list(), [32, 42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'insert_after'. Inserting after element not from list.")

    # ----------------------------------------------------------------------------------------------

    def test_add_in_head(self):
        test_list = prepare_list()
        test_list.add_in_head(DoublyLinkedNode(13))
        self.assertEqual(test_list.to_values_list(), [13, 32, 42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'add_in_head'. Inserting in head in normal list.")

    def test_add_in_head_in_empty_list(self):
        test_list = DoublyLinkedList()
        test_list.add_in_head(DoublyLinkedNode(13))
        self.assertEqual(test_list.to_values_list(), [13],
                         "Testing: 'add_in_head'. Inserting in empty list.")

    def test_add_in_head_multiple_values(self):
        test_list = DoublyLinkedList()
        test_list.add_in_head(DoublyLinkedNode(13))
        test_list.add_in_head(DoublyLinkedNode(14))
        test_list.add_in_head(DoublyLinkedNode(15))
        self.assertEqual(test_list.to_values_list(), [15, 14, 13],
                         "Testing: 'add_in_head'. Inserting multiple values.")


if __name__ == '__main__':
    unittest.main()
