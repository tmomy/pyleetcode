#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2018/2/27 1:14


class Link(object):

    def __init__(self):
        # 依赖对象池
        self.depend = [],
        # 被依赖对象池
        self.depended = []


def seq_output(seq:list):
    seq_dict = {}
    for item in seq:
        node, prev = item
        l_node = Link()
        if prev:
            l_node.depend.append(prev)
            prev_node = seq_dict[prev]
            prev_node.depended.append(node)
        seq_dict[node] = l_node

    # todo 遍历


