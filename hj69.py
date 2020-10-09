#encoding: utf-8

def solution():
    x = int(input())
    y = int(input())
    z = int(input())
    a = []
    for _ in range(x):
        a.append(list(map(int, input().split())))

    b = []
    for _ in range(y):
        b.append(list(map(int, input().split())))

    c = []
    for i in range(x):
        c.append([0] * z)
        for j in range(z):
            rt = 0
            for k in range(y):
                rt += a[i][k] * b[k][j]
            c[i][j] = rt

    for line in c:
        for v in line:
            print(v, end=' ')
        print()

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break