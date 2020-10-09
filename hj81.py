#encoding: utf-8

def solution():
    t1 = input()
    t2 = input()
    print('false' if set(t1) - set(t2) else 'true')

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            break