#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2018/2/27 1:14


class Link(object):

    def __init__(self):
        # 依赖对象池
        self.depend = []
        # 被依赖对象池
        self.depended = []
        self.is_install = False


def seq_output(seq: list):
    seq_dict = {}
    seq_list = []
    for item in seq:
        if len(item) == 1:
            node, = item
            prev = None
        else:
            node, prev = item
        l_node = Link()
        if prev:
            l_node.depend.append(prev)
            if prev not in seq_dict:
                seq_dict[prev] = Link()
            prev_node = seq_dict[prev]
            prev_node.depended.append(node)
        seq_dict[node] = l_node
        seq_list.append(node)
    install = []
    # 遍历队列，将没有依赖的元素按原来顺序加入install队列
    for seq in seq_list:
        v = seq_dict[seq]
        if not v.depend:
            # 没有依赖且未安装过的加入安装队列
            install.append(seq)
            # 标记为已安装
            v.is_install = True

    # 遍历队列，将剩下有依赖且未被安装的元素递归安装其依赖池
    for seq in seq_list:
        v = seq_dict[seq]
        if not v.is_install:
            prev_recursive(v, install, seq_dict)
            install.append(seq)
            v.is_install = True
    return install


def prev_recursive(v, install, seq_dict):
    prev = v.depend
    for seq in prev:
        v = seq_dict[seq]
        # 被安装过
        if v.is_install:
            return True
        else:
            prev_recursive(v, install, seq_dict)
            install.append(seq)
            v.is_install = True


if __name__ == '__main__':
    installed = [("QQ", ".NET"), ("Chrome", ".NET"), ("Music",)]
    print(seq_output(installed))

