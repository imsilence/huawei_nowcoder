#encoding: utf-8

'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1
输入
5.5
输出
6
'''

def solution():
    num = float(input())
    print(int(num+0.5))

if __name__ == '__main__':
    solution()