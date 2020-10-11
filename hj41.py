#encoding: utf-8

def solution():
    input()
    weights = map(int, input().split())
    nums = list(map(int, input().split()))
    s = set([0])
    for i, weight in enumerate(weights):
        for _ in range(nums[i]):
            ss = s.copy()
            for w in ss:
                s.add(w + weight)
            
    print(len(s))
    

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            break