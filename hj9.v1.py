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


def solution(txt):
    rt = []
    for i in range(len(txt)-1, -1, -1):
        if txt[i] not in rt:
            rt.append(txt[i])

    print(''.join(rt))


if __name__ == '__main__':
    txt = input()
    solution(txt)