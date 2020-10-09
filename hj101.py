#encoding: utf-8

def solution():
    input()
    nums = list(map(int, input().split()))
    desc = int(input())

    nums.sort(reverse=desc)
    print(' '.join(map(str, nums)))


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break