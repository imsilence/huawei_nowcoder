#encoding: utf-8

'''
题目描述
给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。
输入描述:
整数N，后续N个名字

输出描述:
每个名称可能的最大漂亮程度

示例1
输入
2
zhangsan
lisi
输出
192
101
'''


from collections import defaultdict

def solution():

    n = int(input())
    for _ in range(n):
        txt = input()
        stats = defaultdict(int)
        for ch in txt.lower():
            stats[ch] += 1

        values = sorted(stats.values(), reverse=True)
        degree = 0
        currentDegree = 26
        for v in values:
            degree += v * currentDegree
            currentDegree -= 1

        print(degree)


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break