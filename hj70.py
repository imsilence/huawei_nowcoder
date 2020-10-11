#encoding: utf-8

'''
题目描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。


例如：

    A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

 

计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。

 

编写程序计算不同的计算顺序需要进行的乘法次数

 

 

 

 

输入描述:
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则

输出描述:
输出需要进行的乘法次数

示例1
输入
3
50 10
10 20
20 5
(A(BC))
输出
3500
'''
class Stack:
    def __init__(self):
        self._values = []
    
    def push(self, v):
        self._values.append(v)
    
    def pop(self):
        return None if self.empty() else self._values.pop(-1)
    
    def empty(self):
        return len(self._values) == 0
    
    def top(self):
        return None if self.empty() else self._values[-1]

def count(a, b):
    return a[0] * a[1] * b[1], [a[0], b[1]]

def solution():
    n = int(input())
    matrix = {}
    for i in range(n):
       matrix[chr(ord('A') + i)] = list(map(int, input().split()))
    expression = input()
    matrixStack = Stack()
    opStack = Stack()
    cnt = 0
    for ch in expression[:-1]:
        if ch == '(':
            opStack.push(ch)
        elif ch == ')':
            right = matrixStack.pop()
            left = matrixStack.pop()
            leftMatrix, rightMatrix = matrix[left], matrix[right]
            cnt += leftMatrix[0] * leftMatrix[1] * rightMatrix[1]
            matrix[left+right] = [leftMatrix[0], rightMatrix[1]]
            opStack.pop()
            matrixStack.push(left+right)
        else:
            matrixStack.push(ch)
    
    print(cnt)

if __name__ == '__main__':
     while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break