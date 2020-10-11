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

1 3 4 0 7 0 0 0 0
0 0 0 0 9 0 0 0 0
8 5 0 0 0 3 0 7 4
0 4 3 0 8 0 6 5 0
0 1 2 3 0 6 0 9 7
7 0 8 2 0 9 4 0 3
2 8 5 6 1 0 3 4 9
0 7 1 0 2 4 5 0 6
4 9 6 5 0 8 0 2 1
'''
def printTable(matrix):
    for line in matrix:
        print(' '.join(map(str, line)))

def line(matrix, i, length):
    nums = [0] * length
    for idx in range(length):
        if matrix[i][idx] != 0:
            nums[matrix[i][idx]-1] = 1
    choices = []
    for idx, v in enumerate(nums):
        if v == 0:
            choices.append(idx + 1)
    return choices


def column(matrix, j, length):
    nums = [0]*length

    for idx in range(length):
        if matrix[idx][j] != 0:
            nums[matrix[idx][j]-1] = 1
    
    choices = []
    for idx, v in enumerate(nums):
        if v == 0:
            choices.append(idx + 1)
    return choices

def block(matrix, no, length):
    nums = [0]*length
    x, y = (no // 3) * 3, (no % 3) * 3 
    for idx in range(length):
        px, py = x + idx //3, y + idx % 3
        if matrix[px][py] != 0:
            nums[matrix[px][py]-1] = 1
    
    choices = []
    for idx, v in enumerate(nums):
        if v == 0:
            choices.append(idx + 1)
    return choices

def restoration(empty, currentPoint, value):
    newEmpty = {}
    for point, choices in empty.items():
        newChoices = []
        for i in range(3):
            newChoices.append(choices[i][:])
            if point[i] == currentPoint[i]:
                newChoices[i].remove(value)
        newEmpty[point] = newChoices
                
    return newEmpty


def solution():
    length = 9
    matrix = []
    empty = {}
    for i in range(length):
        lineValue = [0] * length
        for j, v in enumerate(input().split()):
            value = int(v)
            lineValue[j] = value
            if value == 0:
                empty[(i, j ,i//3 * 3 + j // 3,)] = []
        matrix.append(lineValue)

    for i, j, no in empty:
        empty[(i, j, no, )] = [
            line(matrix, i, length),
            column(matrix, j, length),
            block(matrix, no, length),
        ]

    
    while empty:
        delPoints = {}
        for point, choices in empty.items():
            value = 0
            for choice in choices:
                if len(choice) == 1:
                    value = choice[0]

            if value == 0:
                values = list(set(choices[0]) & set(choices[1]) & set(choices[2]))
                if len(values) == 1:
                    value = values[0]
            
            if value != 0:
                matrix[point[0]][point[1]] = value
                delPoints[point] = value
                break

        for point, value in delPoints.items():
            del empty[point]
            empty = restoration(empty, point, value)

                
    printTable(matrix)

if __name__ == '__main__':
    while True:
        try:
            solution()
        except:
            break