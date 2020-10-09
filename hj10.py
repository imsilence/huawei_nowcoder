#encoding: utf-8

def solution(txt):
    chars = {}
    for ch in txt:
        if ord(ch) <= 127:
            chars[ch] = 1
    print(len(chars))

if __name__ == '__main__':
    txt = input()
    solution(txt)