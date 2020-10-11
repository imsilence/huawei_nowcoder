#encoding: utf-8

def solution(txt):
    nodes = txt.split(';')
    point = [0, 0]
    units = {
        'A' : [-1, 0],
        'D' : [1, 0],
        'W' : [0, 1],
        'S' : [0, -1]
    }
    for node in nodes:
        if node == '':
            continue

        unit = units.get(node[0])
   
        if unit is None:
            continue
        
        distance = 0
        try:
            distance = int(node[1:])
        except Exception:
            continue

        if distance < 0 or distance >= 100:
            continue

        point[0] += unit[0] * distance
        point[1] += unit[1] * distance
    
    print('{0[0]},{0[1]}'.format(point))



if __name__ == '__main__':
    while True:
        try:
            txt = input()
            if txt == '':
                break
            solution(txt)
        except Exception:
            break