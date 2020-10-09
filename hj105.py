#encoding: utf-8

def solution():
    total = 0
    ncnt = 0
    ecnt = 0
    while True:
        try:
            num = int(input())
            if num < 0:
                ncnt += 1
            elif num >= 0:
                total += num
                ecnt += 1
        except Exception as e:
            print(e)
            break


    print("{}\n{:.1f}".format(ncnt, total/ecnt if ecnt > 0 else 0))


if __name__ == '__main__':
    solution()