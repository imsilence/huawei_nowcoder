#encoding: utf-8

'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
180
输出
2 2 3 3 5
'''
def solution():
    num = int(input())
    while num != 1:
        for c in range(2, num+1):
            if num % c == 0:
                num = int(num / c)
                print(c, end=' ')
                break

if __name__ == '__main__':
    solution()