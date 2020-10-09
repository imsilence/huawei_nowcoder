#encoding: utf-8

def solution():
    n = int(input())
    total = 0
    ncnt = 0
    ecnt = 0
    nums = map(int, input().split())
    # for _ in range(n):
    #     num = int(input())
    for num in nums:
        if num < 0:
            ncnt += 1
        elif num > 0:
            total += num
            ecnt += 1

    print("{} {:.1f}".format(ncnt, total/ecnt if ecnt > 0 else 0))


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break