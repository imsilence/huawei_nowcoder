#encoding: utf-8

'''
题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。


处理：


1、 记录最多8条错误记录，循环记录（或者说最后只输出最后出现的八条错误记录），对相同的错误记录（净文件名（保留最后16位）称和行号完全匹配）只记录一条，错误计数增加；


2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；


3、 输入的文件可能带路径，记录文件名称不能带路径。


输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

示例1
输入
复制
E:\V1R2\product\fpgadrive.c   1325
输出
复制
fpgadrive.c 1325 1
'''

import sys
from os import path as filepath
from collections import namedtuple

FileNameLength = 16
MaxSize = 8

def filename(path):
    pos = path.rfind('\\')
    if pos > 0:
        path = path[pos+1:]

    pos = path.rfind('/')
    if pos > 0:
        path = path[pos+1:]

    length = len(path)
    if length <= FileNameLength:
       return path
    return path[length-FileNameLength:]

class Frame:

    def __init__(self, size=8):
        self.__id = 0
        self.__ids = {}
        self.__errors = {}
        self.__size = size
    
    def add(self, f):
        cnt = self.__errors.get(f, 0)
        if cnt == 0:
            self.__errors[f] = 1

            self.__ids[self.__id] = f
            self.__id += 1
        else:
            self.__errors[f] += 1
        
    def __str__(self):
        lines = []
        start = self.__id - self.__size
        if start < 0:
            start = 0
        for i in range(start, self.__id):
            f = self.__ids[i]
            lines.append("{} {} {}".format(f.name, f.line, self.__errors[f]))
        return '\n'.join(lines)

def solution():
    File = namedtuple('File', ['name', 'line'])
    frame = Frame(size=MaxSize)
    line = ''
    while True:
        try:
            line = input()
        except Exception:
            break
        if line == '':
            break
        path, lineNo = line.split()
        frame.add(File(filename(path), lineNo))
    
    print(frame)


if __name__ == '__main__':
    solution()