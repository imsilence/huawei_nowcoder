#encoding: utf-8

def solution(txt):
    n1, n2 = txt.split()
    n1, n2 = int(n1), int(n2)
    rt = []
    while True:
        for i in range(2, max(n1, n2)):
            if n1 % i == 0 and n2 % i == 0:
                rt.append(i)
                n1 //= i
                n2 //= i
                break
        else:
            break

    b = n1 * n2
    for i in rt:
        b *= i
    print(b)
        
if __name__ == '__main__':
     while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except Exception as e:
            import traceback
            traceback.print_exc()
            break