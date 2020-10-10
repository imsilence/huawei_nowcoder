#encoding: utf-8

def ipv4(txt):
    nodes = txt.split('.')
    if len(nodes) != 4:
        return False

    try:
        for node in nodes:
            nodeInt = int(node)
            if str(nodeInt) != node:
                return False
            if nodeInt < 0 or nodeInt > 255:
                return False
        return True
    except Exception:
        return False

    return True

def solution(txt):
    print('YES' if ipv4(txt) else 'NO')


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