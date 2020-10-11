#encoding: utf-8

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