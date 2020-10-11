#encoding: utf-8

'''
题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
4
0 1
0 2
1 2
3 4
输出
0 3
1 2
3 4
'''
def solution():
    n = int(input())
    min, max = 0, 0
    rs = {}
    for _ in range(n):
        i, v = list(map(int, str(input()).split()))
        if i < min:
            min = i
        if i > max:
            max = i
        rs[i] = rs.get(i, 0) + v
    
    for i in range(min, max+1):
        v = rs.get(i, 0)
        if v > 0:
            print(i, v)

if __name__ == '__main__':
    solution()