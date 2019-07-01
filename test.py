# -*- coding: utf-8 -*-


import unittest
from main import *


def prepare_list():
    result = LinkedList2()
    result.add_in_tail(Node(32))
    result.add_in_tail(Node(42))
    result.add_in_tail(Node(12))
    result.add_in_tail(Node(45))
    result.add_in_tail(Node(47))
    result.add_in_tail(Node(49))
    result.add_in_tail(Node(24))
    result.add_in_tail(Node(32))
    result.add_in_tail(Node(11))
    result.add_in_tail(Node(55))

    return result


def check_element_pointers(linked_list, check_list):
    normal_queue_ok = linked_list.to_values_list() == check_list
    reversed_queue_ok = linked_list.to_values_list( reversed=True ) == check_list[::-1]
    return normal_queue_ok and reversed_queue_ok


class MyTestCase(unittest.TestCase):
    # ---------- DELETE TESTS ----------------------------------------------------
    def test_delete(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.delete(12)
        result_list = [32, 42, 45, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete'. Normal case. Wrong result straight arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete'. Normal case. Wrong result reversed arrays.")

    def test_delete_head_element(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.delete(32)
        result_list = [42, 12, 45, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete'. Deleting head element. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete'. Deleting head element. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, test_list.get(0),
                         "Testing: 'delete'. Deleting head element. Incorrect head pointer.")

    def test_delete_tail_element(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.delete(55)
        result_list = [32, 42, 12, 45, 47, 49, 24, 32, 11]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete'. Deleting tail element. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete'. Deleting tail element. Wrong result reversed arrays.")
        self.assertEqual(test_list.tail, test_list.get(8),
                         "Testing: 'delete'. Deleting tail element. Incorrect tail pointer.")

    def test_delete_from_empty_list(self):
        test_list = LinkedList2()
        test_list.delete(55)
        result_list = []
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete'. Trying to delete from empty list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), [],
                         "Testing: 'delete'. Trying to delete from empty list. Wrong result reversed arrays.")

    def test_delete_which_not_present(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.delete(66)
        result_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete'. Trying delete node from that list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete'. Trying delete node from that list. Wrong result reversed arrays.")

    # ---------- DELETE ALL TESTS ----------------------------------------------------

    def test_delete_all(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 12, 32, 11, 55, 32]
        test_list = LinkedList2(base_list)
        test_list.delete(12, all=True)
        result_list = [32, 42, 45, 47, 49, 24, 32, 11, 55, 32]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete all'. Normal case. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete all'. Normal case. Wrong result reversed arrays.")

    def test_delete_all_elements_in_head_and_tail(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 12, 32, 11, 55, 32]
        test_list = LinkedList2(base_list)
        test_list.delete(32, all=True)
        result_list = [42, 12, 45, 47, 49, 24, 12, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete all'. Deleting from head and tail case. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete all'. Deleting from head and tail case. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, test_list.get(0),
                         "Testing: 'delete all'. Deleting from head and tail case. Incorrect head pointer.")
        self.assertEqual(test_list.tail, test_list.get(8),
                         "Testing: 'delete all'. Deleting from head and tail case. Incorrect tail pointer.")

    def test_delete_all_elements_goes_one_by_one(self):
        base_list = [32, 42, 12, 45, 45, 47, 49, 24, 45, 45, 45, 12, 32, 11, 55, 32]
        test_list = LinkedList2(base_list)
        test_list.delete(45, all=True)
        result_list = [32, 42, 12, 47, 49, 24, 12, 32, 11, 55, 32]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete all'. Deleting elements which comes one by one. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete all'. Deleting elements which comes one by one. Wrong result reversed arrays.")

    def test_delete_all_elements_goes_one_by_one_in_head_and_tail(self):
        base_list = [32, 32, 32, 42, 12, 45, 47, 49, 24, 12, 11, 55, 32, 32]
        test_list = LinkedList2(base_list)
        test_list.delete(32, all=True)
        result_list = [42, 12, 45, 47, 49, 24, 12, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'delete all'.\n"
                         "Deleting elements which comes one by one in head and tail.\n"
                         "Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'delete all'.\n"
                         "Deleting elements which comes one by one in head and tail.\n"
                         "Wrong result reversed arrays.")
        self.assertEqual(test_list.head, test_list.get(0),
                         "Testing: 'delete all'.\n"
                         "Deleting elements which comes one by one in head and tail.\n"
                         "Incorrect head pointer.")
        self.assertEqual(test_list.tail, test_list.get(8),
                         "Testing: 'delete all'.\n"
                         "Deleting elements which comes one by one in head and tail.\n"
                         "Incorrect tail pointer.")

    # ---------- INSERT TESTS ----------------------------------------------------

    def test_insert(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.insert(test_list.get(3), Node(50))
        result_list = [32, 42, 12, 45, 50, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'insert'. Inserting in middle of list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'insert'. Inserting in middle of list. Wrong result reversed arrays.")

    def test_insert_head(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.insert(test_list.get(0), Node(50))
        result_list = [32, 50, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'insert'. Inserting after head element of list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'insert'. Inserting after head element of list. Wrong result reversed arrays.")

    def test_insert_tail(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_node = Node(50)
        test_list.insert(test_list.get(9), test_node)
        result_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55, 50]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'insert'. Inserting in tail. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'insert'. Inserting in tail. Wrong result reversed arrays.")
        self.assertEqual(test_list.tail, test_node,
                         "Testing: 'insert'. Inserting in tail. Incorrect tail pointer.")

    def test_insert_none_element_in_not_empty_list(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_node = Node(50)
        test_list.insert(None, test_node)
        result_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55, 50]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'insert'. Inserting after none element of list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'insert'. Inserting after none element of list. Wrong result reversed arrays.")
        self.assertEqual(test_node, test_list.tail,
                         "Testing 'insert'. Inserting after none element of list. Incorrect tail pointer.")

    def test_insert_none_element_in_empty_list(self):
        test_list = LinkedList2()
        test_node = Node(50)
        test_list.insert(None, test_node)
        result_list = [50]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'insert'. Inserting after none element of list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'insert'. Inserting after none element of list. Wrong result reversed arrays.")
        self.assertEqual(test_list.tail, test_node,
                         "Testing: 'insert'. Inserting after none element of list. Incorrect tail pointer.")
        self.assertEqual(test_list.head, test_node,
                         "Testing: 'insert'. Inserting after none element of list. Incorrect head pointer.")

    def test_insert_element_not_from_list(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_list.insert(Node(10), Node(50))
        result_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'insert'. Inserting after element not from list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'insert'. Inserting after element not from list. Wrong result reversed arrays.")

    # ---------- ADD IN HEAD TESTS ----------------------------------------------------

    def test_add_in_head(self):
        base_list = [32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        test_list = LinkedList2(base_list)
        test_node = Node(13)
        test_list.add_in_head(test_node)
        result_list = [13, 32, 42, 12, 45, 47, 49, 24, 32, 11, 55]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'add_in_head'. Inserting in head in normal list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'add_in_head'. Inserting in head in normal list. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, test_node,
                         "Testing: 'add_in_head'. Inserting in head in normal list. Incorrect head pointer.")

    def test_add_in_head_in_empty_list(self):
        test_list = LinkedList2()
        test_node = Node(13)
        test_list.add_in_head(test_node)
        result_list = [13]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'add_in_head'. Inserting in empty list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'add_in_head'. Inserting in empty list. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, test_node,
                         "Testing: 'add_in_head'. Inserting in empty list. Wrong result arrays.")
        self.assertEqual(test_list.tail, test_node,
                         "Testing: 'add_in_head'. Inserting in empty list. Wrong result arrays.")

    def test_add_in_head_multiple_values(self):
        test_list = LinkedList2()
        test_list.add_in_head(Node(13))
        test_list.add_in_head(Node(14))
        test_list.add_in_head(Node(15))
        result_list = [15, 14, 13]
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'add_in_head'. Inserting multiple values. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'add_in_head'. Inserting multiple values. Wrong result reversed arrays.")

    # ---------- CLEAN TESTS ----------------------------------------------------

    def test_clean_simple_list(self):
        test_list = LinkedList2()
        test_list.add_in_head(Node(13))
        test_list.add_in_head(Node(14))
        test_list.add_in_head(Node(15))
        test_list.clean()
        result_list = []
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'clean'. Cleaning simple list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'clean'. Cleaning simple list. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, None,
                         "Testing: 'clean'. Cleaning simple list. Head is not None.")
        self.assertEqual(test_list.tail, None,
                         "Testing: 'clean'. Cleaning simple list. Tail is not None.")

    def test_clean_list_with_single_element(self):
        test_list = LinkedList2()
        test_list.add_in_head(Node(13))
        test_list.clean()
        result_list = []
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'clean'. Cleaning list with single element. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'clean'. Cleaning list with single element. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, None,
                         "Testing: 'clean'. Cleaning list with single element. Head is not None.")
        self.assertEqual(test_list.tail, None,
                         "Testing: 'clean'. Cleaning list with single element. Tail is not None.")

    def test_clean_empty_list(self):
        test_list = LinkedList2()
        test_list.clean()
        result_list = []
        self.assertEqual(test_list.to_values_list(), result_list,
                         "Testing: 'clean'. Cleaning empty list. Wrong result arrays.")
        self.assertEqual(test_list.to_values_list(reversed=True), result_list[::-1],
                         "Testing: 'clean'. Cleaning empty list. Wrong result reversed arrays.")
        self.assertEqual(test_list.head, None,
                         "Testing: 'clean'. Cleaning empty list. Head is not None.")
        self.assertEqual(test_list.tail, None,
                         "Testing: 'clean'. Cleaning empty list. Tail is not None.")

    # ---------- LEN TESTS ----------------------------------------------------

    def test_len_normal_list(self):
        test_list = LinkedList2()
        test_list.add_in_head(Node(13))
        test_list.add_in_head(Node(14))
        test_list.add_in_head(Node(15))
        result_len = 3
        test_len = test_list.len()
        self.assertEqual(test_len, result_len,
                         "Testing: 'len'. Receiving len of normal list. Incorrect len value.")

    def test_len_empty_list(self):
        test_list = LinkedList2()
        result_len = 0
        test_len = test_list.len()
        self.assertEqual(test_len, result_len,
                         "Testing: 'len'. Receiving len of empty list. Incorrect len value.")


if __name__ == '__main__':
    unittest.main()
