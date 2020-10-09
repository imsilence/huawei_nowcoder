#encoding: utf-8

def getContains(lst, value):
    rt = []
    for i, v in enumerate(lst):
        if value in v:
            rt.append(str(i))
            rt.append(v)
    return rt

def solution():
    iList = input().split()[1:]
    rList = list(set(input().split()[1:]))
    rList.sort(key=lambda x: int(x))
    # print(iList, rList)
    rt = []
    for value in rList:
        contains = getContains(iList, value)
        if not contains:
            continue
        rt.append(value)
        rt.append(str(len(contains)//2))
        rt.extend(contains)

    print("{} {}".format(len(rt), ' '.join(rt)))

if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break