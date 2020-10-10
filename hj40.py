#encoding: utf-8

def solution(txt):
    stat = {
        'alpha' : 0,
        'digit' : 0,
        'empty' : 0,
        'other' : 0,
    }
    for ch in txt:
        if ch.isalpha():
            stat['alpha'] += 1
        elif ch.isdigit():
            stat['alpha'] += 1
        elif ch == ' ':
            stat['empty'] += 1
        else:
            stat['other'] += 1

    # print("{alpha} {empty} {digit} {other}".format(**stat))
    print(stat['alpha'])
    print(stat['empty'])
    print(stat['digit'])
    print(stat['other'])




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