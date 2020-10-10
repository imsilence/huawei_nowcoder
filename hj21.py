#encoding: utf-8

def solution(txt):
    uppers = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'bcdefghijklmnopqrstuvwxyza'))
    lowers = dict(zip('abcdefghijklmnopqrstuvwxyz', '22233344455566677778889999'))

    rt = []
    for ch in txt:
        if ch >= 'A' and ch <= 'Z':
            rt.append(uppers.get(ch))
        elif ch >= 'a' and ch <= 'z':
            rt.append(lowers.get(ch))
        elif ch >= '0' and ch <= '9':
            rt.append(ch)

    print(''.join(rt))

if __name__ == '__main__':
    txt = input()
    solution(txt)