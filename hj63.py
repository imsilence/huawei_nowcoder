#encoding: utf-8
'''
题目描述
一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。

给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。
 

输入描述:
输入一个string型基因序列，和int型子串的长度

输出描述:
找出GC比例最高的子串,如果有多个输出第一个的子串

示例1
输入
AACTGTGCACGACCTGA
5
输出
GCACG
'''
from collections import defaultdict

def gcCount(txt):
    gc = 0
    for ch in txt:
        if ch == 'G' or ch == 'C':
            gc += 1
    return gc

def solution():
    txt = input()
    n = int(input())
    stats = defaultdict(list)
    if len(txt) == n:
        stats[gcCount(txt)] = [txt]

    for i in range(len(txt) - n):
        substr = txt[i:i+n]
        stats[gcCount(substr)].append(substr)
    
    return stats[max(stats)][0]

if __name__ == '__main__':
    while True:
        try:
            print(solution())
        except Exception as e:
            import traceback
            traceback.print_exc()
            break