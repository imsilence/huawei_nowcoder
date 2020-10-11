#encoding: utf-8

'''
题目描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)读入
数据范围小于1e6
输入描述:
输入任意个整数

输出描述:
输出负数个数以及所有非负数的平均值

示例1
输入
-13
-4
-7
输出
3
0.0
'''
def solution():
    total = 0
    ncnt = 0
    ecnt = 0
    while True:
        try:
            num = int(input())
            if num < 0:
                ncnt += 1
            elif num >= 0:
                total += num
                ecnt += 1
        except Exception as e:
            print(e)
            break


    print("{}\n{:.1f}".format(ncnt, total/ecnt if ecnt > 0 else 0))


if __name__ == '__main__':
    solution()