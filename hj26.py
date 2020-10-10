#encoding: utf-8

def solution(txt):
    chars = list(txt)
    idxs = []
    for idx, ch in enumerate(chars):
        if ch.isalpha():
            idxs.append(idx)
    for j in range(len(idxs)-1):
        for i in range(len(idxs)-1-j):
            if chars[idxs[i]].lower() > chars[idxs[i+1]].lower():
                chars[idxs[i]], chars[idxs[i+1]] = chars[idxs[i+1]], chars[idxs[i]]

    print(''.join(chars))

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