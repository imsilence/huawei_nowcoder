#encoding: utf-8

def solution():
    m, n = input().split()
    rt = []
    last = -1
    for _ in range(int(m)):
        idTxt, valueTxt = input().split()
        ident, value = int(idTxt), int(valueTxt)
        if last < 0:
            rt.append(value)
            last = ident
        elif ident <= last:
            continue
        elif ident - last == 1:
            rt.append(value)
            last = ident
        else:
            length = ident - last
            k = (value - rt[-1]) / length
            for i in range(length):
                rt.append(int(k * (i+1)))
            rt.append(value)
            last = ident
    print('-----')
    print(rt)
    n = min(int(n), len(rt))
    for i in range(n):
        print(last - n + i + 1, rt[-n+i])



if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break