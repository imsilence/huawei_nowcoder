#encoding: utf-8

def solution(num):
    if num * 10 % 10 >= 5:
        print(int(num) + 1)
    else:
        print(int(num))

if __name__ == '__main__':
     while True:
        try:
            txt = input()
            if txt == '':
                break
            num = float(txt)
            solution(num)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break