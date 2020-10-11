#encoding: utf-8

'''
题目描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。

输入描述:
首先输入一个正整数n，
然后输入n个整数。

输出描述:
输出负数的个数，和所有正整数的平均值。

示例1
输入
5
1
2
3
4
5
输出
0 3.0
'''
def solution():
    n = int(input())
    total = 0
    ncnt = 0
    ecnt = 0
    nums = map(int, input().split())
    # for _ in range(n):
    #     num = int(input())
    for num in nums:
        if num < 0:
            ncnt += 1
        elif num > 0:
            total += num
            ecnt += 1

    print("{} {:.1f}".format(ncnt, total/ecnt if ecnt > 0 else 0))


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break