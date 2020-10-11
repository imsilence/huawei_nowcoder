#encoding: utf-8

'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
9876673
输出
37689
'''

def solution():
    nums = [0] * 10
    newNum = 0

    num = int(input())
    while num != 0:
        nextNum = num % 10
        num //= 10

        if nums[nextNum] > 0:
            continue
        nums[nextNum] = 1

        newNum = newNum * 10 + nextNum
    print(newNum)

if __name__ == '__main__':
    solution()