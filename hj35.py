#encoding: utf-8

def solution(num):
    rt = [[0] * num for _ in range(num)]
    idx = 1
    for i in range(num):
        for j in range(0, i+1):
            rt[i-j][j] = idx
            idx += 1

    for line in rt:
        print(' '.join([str(x) for x in line if x != 0]))

if __name__ == '__main__':
     while True:
        try:
            txt = input()
            if txt == '':
                break
            num = int(txt)
            solution(num)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break