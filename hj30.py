#encoding: utf-8

def tf(ch):
    r = {
        '0' : '0', #0000 -> 0000
        '1' : '8', #0001 -> 1000
        '2' : '4', #0010 -> 0100
        '3' : 'C', #0011 -> 1100
        '4' : '2', #0100 -> 0010
        '5' : 'A', #0101-> 1010
        '6' : '6', #0110 -> 0110
        '7' : 'E', #0111 -> 1110
        '8' : '1', #1000 -> 0001
        '9' : '9', #1001 -> 1001
        'a' : '5', #1010 -> 0101
        'b' : 'D', #1011 -> 1101
        'c' : '3', #1100 -> 0011
        'd' : 'B', #1101 -> 1011
        'e' : '7', #1110 -> 0111
        'f' : 'F', #1111 -> 1111
        'A' : '5', #1010 -> 0101
        'B' : 'D', #1011 -> 1101
        'C' : '3', #1100 -> 0011
        'D' : 'B', #1101 -> 1011
        'E' : '7', #1110 -> 0111
        'F' : 'F', #1111 -> 1111
    }
    return r.get(ch, ch)

def solution(txt):
    s1, s2 = txt.split()
    chars = list(s1) + list(s2)
    odds = sorted(chars[::2])
    evens = sorted(chars[1::2])
    i = 0
    rt = []
    while i < len(odds) or i < len(evens):
        odd = odds[i] if i < len(odds) else ''
        even = evens[i] if i < len(evens) else ''
        i += 1
        rt.append(tf(odd))
        rt.append(tf(even))
    
    return ''.join(rt)


if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            print(solution(txt))
        except Exception:
            break
