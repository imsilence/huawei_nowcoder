#encoding: utf-8

'''
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1
输入
abcdd
输出
dd
'''
from collections import defaultdict

def solution(txt):
    stats = defaultdict(int)
    for ch in txt:
        stats[ch] += 1
    
    nums = defaultdict(dict)
    minCount = 200
    for k, v in stats.items():
        nums[v][k] = True
        if v < minCount:
            minCount = v
    
    chars = nums.get(minCount)
    if chars:
        rt = []
        for ch in txt:
            if chars.get(ch):
                continue
            rt.append(ch)
        return ''.join(rt)
    
    return txt


if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            print(solution(txt))
        except Exception:
            break