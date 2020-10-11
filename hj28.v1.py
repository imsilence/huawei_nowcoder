#encoding: utf-8

'''
题目描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。

输出:

输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。

 

输入描述:
输入说明
1 输入一个正偶数n
2 输入n个整数

输出描述:
求得的“最佳方案”组成“素数伴侣”的对数。

示例1
输入
4
2 5 6 13
输出
2
'''

import math

def isPrime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

def sameNodes(selected, node):
    sames = []
    for n in selected:
        if n[0] == node[0] or n[0] == node[1] or n[1] == node[0] or n[1] == node[1]:
            sames.append(n)
    return sames

def findPG(selected, groups, start):
    if start >= len(groups):
        return len(selected)

    node = groups[start]
    sames = sameNodes(selected, node)
    
    if sames:
        cnt = 0
        for same in sames:
            sameSelected = selected[:]
            sameSelected.remove(same)
            sameSelected.append(node)
            c = findPG(sameSelected, groups, start+1)
            if c > cnt:
                cnt = c
        c = findPG(selected, groups, start+1)
        if c > cnt:
            cnt = c
        return cnt
    else:
        selected.append(node)
        return findPG(selected, groups, start+1)
        

def solution():
    length = int(input())
    numbers = list(map(int, input().split()))

    groups = []
    for i in range(0, length):
        for j in range(i+1, length):
            n1, n2 = numbers[i], numbers[j]
            if isPrime(n1 + n2):
                groups.append([n1, n2])
    groups.sort()
    print(findPG([], groups, 0))

if __name__ == '__main__':
    solution()