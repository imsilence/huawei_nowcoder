#encoding: utf-8

def solution():
    txtA = input()
    txtB = input()
    distance = [[0] * (len(txtA) + 1) for i in range(len(txtB) + 1)]
    for i in range(len(txtA) + 1):
        distance[0][i] = i
    for i in range(len(txtB) + 1):
        distance[i][0] = i

    for i in range(1, len(txtA) + 1):
        for j in range(1, len(txtB) + 1):
            if txtA[i-1] == txtB[j-1]:
                distance[j][i] = distance[j-1][i-1]
            else:
                distance[j][i] = min(distance[j-1][i], distance[j][i-1], distance[j-1][i-1]) + 1
    print(distance[-1][-1])

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break