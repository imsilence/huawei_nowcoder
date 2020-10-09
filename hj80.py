#encoding: utf-8

def solution():
    input()
    aList = list(map(int, input().split()))
    input()
    bList = list(map(int, input().split()))
    mergeList = list(set(aList + bList))
    mergeList.sort()
    print(''.join(map(str, mergeList)))

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            break