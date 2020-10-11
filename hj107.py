#encoding: utf-8

'''
题目描述
•计算一个数字的立方根，不使用库函数

详细描述：

•接口说明

原型：

public static double getCubeRoot(double input)

输入:double 待求解参数

返回值:double  输入参数的立方根，保留一位小数


输入描述:
待求解参数 double类型

输出描述:
输入参数的立方根 也是double类型

示例1
输入
216
输出
6.0
'''
import math

def solution(num):
    start = 0
    end = num
    middle = 0
    while True:
        middle = (end + start) / 2
        tmp = middle ** 3
        if math.fabs(tmp - num) <= 0.0005:
            break
        elif tmp > num:
            end = middle
        elif tmp < num:
            start = middle

    print("{:.1f}".format(middle))

if __name__ == '__main__':
    num = float(input())
    solution(num)