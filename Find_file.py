# _*_coding:utf-8_*_
import os


def find_file(file_path, file_name):
    for i in os.listdir(file_path):  # 遍历目录
        if os.path.isdir(i):  # 若是目录，则进入递归
            find_file(os.path.join(file_path, i), file_name)
        elif os.path.basename(i).find(file_name) != -1:  # 判断是否包含目标信息
            print(os.path.join(file_path, i))
find_file('C:\GitHub\Python-Training', 'hello')
