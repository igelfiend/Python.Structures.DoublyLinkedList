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
        test_list.remove_by_value(32)
        self.assertEqual(test_list.to_values_list(), [42, 12, 45, 47, 49, 24, 32, 11, 55],
                         "Testing: 'remove_by_value'. Normal case.")


if __name__ == '__main__':
    unittest.main()
