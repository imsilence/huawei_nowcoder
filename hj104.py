#encoding: utf-8

def solution():
    n = int(input())
    for _ in range(n):
        txt = input()
        if txt == '':
            return
        start = 0
        while start < len(txt):
            d = txt[start:start+8]
            print(d+'0'*(8-len(d)))
            start += 8

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break