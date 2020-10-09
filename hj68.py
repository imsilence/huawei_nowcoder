#encoding: utf-8

def solution():
    n = int(input())
    asc = int(input())
    rt = []
    for _ in range(n):
        name, value = input().split()
        rt.append([name, int(value)])

    rt.sort(key=lambda x: x[1], reverse=not asc)

    for name, value in rt:
        print(name, value)


if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            break