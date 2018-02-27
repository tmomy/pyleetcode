#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2018/2/27 8:06

import unittest

from src.sequence_output import seq_output


class TestSequenceOutput(unittest.TestCase):

    def test_seq_output(self):
        installed = [("QQ",".NET"), ("Chrome",".NET"), ("Music",)]
        actual = seq_output(installed)
        expect = ['Music', '.NET', 'QQ', 'Chrome']
        self.assertEqual(expect, actual)