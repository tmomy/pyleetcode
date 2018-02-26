#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2018/2/26 22:59
import os
import time


# def follow(file_dir, file_num, file_name):
#     """
#     输出最新文件内容
#     :param file_dir:  监控文件所处文件夹 eg: D:/log/
#     :param file_num:  监控文件夹下文件数量
#     :param file_name: 监控文件文件名
#     :return:
#     """
#     print(222)
#     file_path = os.path.join(file_dir,file_name)
#     f = open(file_path, "r")
#     f.seek(0, 0)
#     new_file_num = 0
#     print(222)
#     while True:
#         line = f.readline()
#         if not line:
#             time.sleep(0.1)
#             # 1s检查文件夹下数量
#             new_file_num = len(os.listdir(file_dir))
#             continue
#         yield line
#         if file_num < new_file_num:
#             # 监控文件夹下文件数量增加，从新读取监控文件
#             follow(file_dir=file_dir, file_num=new_file_num, file_name=file_name)

def follow(the_file):
    the_file.seek(0,0)
    while True:
        line = the_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def path_handle(path):
    # 文件路径合法性检查
    if not os.path.isfile(path):
        return "文件路径不存在"
    file_dir, file_name = os.path.split(path)
    return file_dir, file_name


def file_handle(path):
    file_dir, file_name = path_handle(path)
    file_list = os.listdir(file_dir)
    file_num = len(file_list)
    if file_num > 1:
        sort_files = sorted(file_list, key=lambda ctime: os.path.getctime(ctime),reverse=False)
        for old_file in sort_files[:file_num-1]:
            with open(old_file, "r") as f:
                l = f.readline()
                yield l
    file_paths = os.path.join(file_dir, file_name)
    f = open(file_paths, "r")
    loglines = follow(f)
    for line in loglines:
        yield line


if __name__ == '__main__':
    file_path = "D:\\PythonProject\\pyleetcode\\src\\logs\\test.log"
    ls = file_handle(file_path)
    for l in ls:
        print(l)