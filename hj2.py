#encoding: utf-8

'''
题目描述
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述:
输出输入字符串中含有该字符的个数。

示例1
输入
ABCDEF
A
输出
1
'''

def ignoreCaseCount(text, ch):
    cnt = 0
    lower, upper = ch.lower(), ch.upper()

    for c in text:
        if c == lower or c == upper:
            cnt += 1
    return cnt

def solution():
    print(ignoreCaseCount(input(), input()))


if __name__ == '__main__':
    solution()