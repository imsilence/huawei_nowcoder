#encoding: utf-8

import sys

def allIsOne(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                return False
    return True

def subMatrix(matrix, x, y, z):
    subMatrix = [[0] * z for _ in range(z)]
    for m in range(z):
        for n in range(z):
            subMatrix[m][n] = 1 if matrix[x+m][y+n] == '1' else 0
    return subMatrix


def solution():
    n = int(sys.stdin.readline())
    matrix = []
    for _ in range(n):
        matrix.append(list(sys.stdin.readline().strip()))

    m = len(matrix[0])
    maxArea = 0
    for x in range(n):
        for y in range(m):
            for z in range(min(n-x, m-y)): # 可优化为最大的宽度开始
                if allIsOne(subMatrix(matrix, x, y, z+1), z+1):
                    area = (z+1) ** 2
                    if maxArea < area:
                        maxArea = area
    print(maxArea)


if __name__ == '__main__':
    solution()