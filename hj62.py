#encoding: utf-8

def solution(num):
    cnt = 0
    while num:
        if num % 2:
            cnt += 1
        num >>= 1

    print(cnt)


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