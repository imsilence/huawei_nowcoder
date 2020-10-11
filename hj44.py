#encoding: utf-8

'''
题目描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组

输入描述:
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述:
完整的9X9盘面数组

示例1
输入
复制
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
输出
复制
5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1
'''


choices = list(map(int, '123456789'))

def printTable(matrix):
    for line in matrix:
        print(' '.join(map(str, line)))

def check(matrix, i, j, num, length):
    px, py = (i // 3) * 3, (j // 3) * 3
    for x in range(length):
        if x != i and matrix[x][j] == num:
            return False
        if x != j and matrix[i][x] == num:
            return False
        pi, pj = px + x // 3, py + x % 3
        if (pi != i or pj != j) and matrix[pi][pj] == num:
            return False
        
    return True


def dfs(matrix, length):
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == 0:
                for num in choices:
                    matrix[i][j] = num
                    if check(matrix, i, j, num, length) and dfs(matrix, length):
                        return True
                    matrix[i][j] = 0
                return False
    return True

def solution():
    length = 9
    matrix = []
    for _ in range(length):
        matrix.append(list(map(int, input().split())))
    
    dfs(matrix, length)
                
    printTable(matrix)

if __name__ == '__main__':
    while True:
        try:
            solution()
        except:
            break