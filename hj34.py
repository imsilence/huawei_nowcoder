#encoding: utf-8

def solution(txt):
    print(''.join(sorted(txt)))

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