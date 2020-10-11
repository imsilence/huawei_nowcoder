#encoding: utf-8

'''
题目描述
找出字符串中第一个只出现一次的字符

 

 

 

输入描述:
输入几个非空字符串

输出描述:
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入
asdfasdfo
aabb
输出
o
-1
'''

def solution(txt):
    stats = {}
    chars = []
    for ch in txt:
        if ch in stats:
            stats[ch] += 1
        else:
            chars.append(ch)
            stats[ch] = 1
    
    for ch in chars:
        if stats.get(ch) == 1:
            return ch
    return -1

if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            print(solution(txt))
        except Exception as e:
            import traceback
            traceback.print_exc()
            break