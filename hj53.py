#encoding: utf-8

'''
题目描述
1

1  1  1

1  2  3  2  1

1  3  6  7  6  3  1

1  4  10 16 19  16 10  4  1

以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。

求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3。


输入n(n <= 1000000000)
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)等方式读入
输入描述:
输入一个int整数

输出描述:
输出返回的int值

示例1
输入
4
输出
3
'''

def solution(layer):
    if layer < 2:
        return -1
    column = 2 * layer - 1
    middle = column // 2
    matrix = [[0] * column for _ in range(layer)]
    matrix[0][middle] = 1
    def getValue(i, j):
        if i < 0 or i >= layer:
            return 0
        elif j < 0 or j >= 2*layer-1:
            return 0
        else:
            return matrix[i][j]

    for i in range(1, layer):
        for j in range(middle-i, middle+i+1):
            matrix[i][j] = getValue(i-1, j-1) + getValue(i-1, j) + getValue(i-1, j+1)
    
    for idx, num in enumerate(matrix[-1]):
        if num % 2 == 0:
            return idx + 1
    return -1


if __name__ == '__main__':
    while True:
        try:
            print(solution(int(input())))
        except Exception as e:
            print(e)
            break