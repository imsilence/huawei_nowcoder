#encoding: utf-8


def key(word):
    return ''.join(sorted(word))

def solution():
    _, *words, word, index = input().split()
    store = {}
    for w in words:
        k =  key(w)
        ws = store.get(k, [])
        ws.append(w)
        store[k] = ws

    k = key(word)
    ws = sorted(store.get(k, []))
    i, cnt, fword = 1, 0, ''

    index = int(index)
    for w in ws:
        if w == word:
            continue
        if i == index:
            fword = w
        cnt += 1
        i += 1

    print(cnt)
    print(fword)

if __name__ == '__main__':
    solution()