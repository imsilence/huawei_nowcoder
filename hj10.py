#encoding: utf-8

'''
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
输入
abaca
输出
3
输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

示例1
输入
abc
输出
3
'''
def solution(txt):
    chars = {}
    for ch in txt:
        if ord(ch) <= 127:
            chars[ch] = 1
    print(len(chars))

if __name__ == '__main__':
    txt = input()
    solution(txt)