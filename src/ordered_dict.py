#!/usr/bin/env python
# encoding: utf-8
"""
@author: Tmomy
@time: 2018/2/26 17:42
"""


# 维持key顺序的双向链表
class Link(object):

    def __init__(self):
        self.prev = None,
        self.next = None,
        self.value = None,
        self.key = None


class SortedDict(dict):

    def __init__(self):
        super(dict, self).__init__()
        self.__head_link = Link()
        self.__head_link.prev = self.__head_link
        self.__head_link.next = self.__head_link
        self.__map = {}

    # 时间复杂度 O(1)
    def __setitem__(self, key, value,link=Link):
        if key not in self.__map:
            self.__map[key] = l = link()
            last = self.__head_link.prev
            self.__head_link.prev = l
            last.next = l
            l.key = key
            l.value = value
            l.prev = last
            l.next = self.__head_link

    # 时间复杂度 O(1)
    def __getitem__(self, item):
        if item in self.__map:
            return self.__map[item].value

    # 时间复杂度 O(1)
    def __delitem__(self, key):
        key_link = self.__map.pop(key)
        key_link_prev = key_link.prev
        key_link_next = key_link.next
        key_link_next.prev = key_link_prev
        key_link_prev.next = key_link_next
        key_link.prev = None
        key_link.next = None
        key_link.value = None
        key_link.key = None

    def __iter__(self):
        root = self.__head_link
        curr = root.next
        while curr is not root:
            yield curr.key
            curr = curr.next

    # 时间复杂度 O(1)
    def popitem(self, last=True):

        if not self.__map:
            raise KeyError('dict is empty')
        if last:
            pop_link = self.__head_link.prev
            link_prev = pop_link.prev
            link_prev.next = self.__head_link
            self.__head_link.prev = link_prev
        else:
            pop_link = self.__head_link.next
            link_next = pop_link.next
            self.__head_link.next = link_next
            link_next.prev = self.__head_link
        key = pop_link.key
        v = self.__map.pop(key)
        return key, v.value

    # 时间复杂度 O(n)
    def keys(self):
        root = self.__head_link
        curr = root.next
        ks = []
        while curr is not root:
            ks.append(curr.key)
            curr = curr.next
        return ks







