#encoding: utf-8

def solution(num):
    cnt = 0
    bits = 0
    while num:
        if num % 2:
            cnt+=1
        else:
            if cnt > bits:
                bits = cnt
            cnt = 0
        num //= 2

    if cnt > bits:
        bits = cnt
    print(bits)


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