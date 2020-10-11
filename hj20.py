#encoding: utf-8

def isWeak(password):
    if len(password) <= 8:
        return True
    
    category = [0] * 4
    for ch in password:
        if ch >= 'a' and ch <= 'z':
            category[0] = 1
        elif ch >= 'A' and ch <= 'Z':
            category[1] = 1
        elif ch >= '0' and ch <= '9':
            category[2] = 1
        else:
            category[3] = 1

    if sum(category) < 3:
        return True

    for i in range(len(password)-3):
        substr = password[i:i+3]
        if substr in password[i+3:]:
            return True
    
    return False

def solution(txt):
    return 'NG' if isWeak(txt) else 'OK'

if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            print(solution(txt))
        except Exception:
            break