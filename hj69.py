#encoding: utf-8

'''
题目描述
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的



输入描述:
输入包含多组数据，每组数据包含：

第一行包含一个正整数x，代表第一个矩阵的行数

第二行包含一个正整数y，代表第一个矩阵的列数和第二个矩阵的行数

第三行包含一个正整数z，代表第二个矩阵的列数

之后x行，每行y个整数，代表第一个矩阵的值

之后y行，每行z个整数，代表第二个矩阵的值



输出描述:
对于每组输入数据，输出x行，每行z个整数，代表两个矩阵相乘的结果
示例1
输入
2
3
2
1 2 3
3 2 1
1 2
2 1
3 3
输出
14 13
10 11
'''

def solution():
    x = int(input())
    y = int(input())
    z = int(input())
    a = []
    for _ in range(x):
        a.append(list(map(int, input().split())))

    b = []
    for _ in range(y):
        b.append(list(map(int, input().split())))

    c = []
    for i in range(x):
        c.append([0] * z)
        for j in range(z):
            rt = 0
            for k in range(y):
                rt += a[i][k] * b[k][j]
            c[i][j] = rt

    for line in c:
        for v in line:
            print(v, end=' ')
        print()

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break