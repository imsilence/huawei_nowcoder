#encoding: utf-8

def solution():
    n = int(input())
    ops = input()
    current = 1
    items = list(range(1, min(n, 4) + 1))
    for op in ops:
        if op == 'U':
            current -= 1
            if current <= 0:
                current += n
                items = list(range(max(1, n-4 + 1), n + 1))
            else:
                if current not in items:
                    items.pop(-1)
                    items.insert(0, current)
        else:
            current += 1
            if current > n:
                current -= n
                items = list(range(1, min(n, 4) + 1))
            else:
                if current not in items:
                    items.pop(0)
                    items.append(current)


    print(' '.join(map(str, items)))
    print(current)


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break