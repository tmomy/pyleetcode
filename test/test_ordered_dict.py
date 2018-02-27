#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2018/2/26 20:52
import unittest

from src.ordered_dict import SortedDict


class TestSortedDict(unittest.TestCase):

    def test_setitem(self):
        d = SortedDict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_delitem(self):
        d = SortedDict()
        d['first'] = "first"
        d['second'] = "second"
        d['third'] = "third"
        expect = ["first", "second", "third"]
        actual = d.keys()
        self.assertEqual(expect, actual)
        d.__delitem__("second")
        del_expect = ["first", "third"]
        del_actual = d.keys()
        self.assertEqual(del_expect, del_actual)

    def test_popitem(self):
        d = SortedDict()
        d['first'] = "first"
        d['second'] = "second"
        d['third'] = "third"
        head_value = d.popitem(False)
        self.assertEqual(head_value, ("first","first"))
        tail_value = d.popitem()
        self.assertEqual(tail_value, ("third","third"))


