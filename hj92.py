#encoding: utf-8

def solution():
    txt = input()
    nums = ""
    currents = []
    rts = []
    for ch in txt:
        if ch >= '0' and ch <= '9':
            currents.append(ch)
        else:
            if len(currents) > len(nums):
                rts = []
                nums = ''.join(currents)
                rts.append(nums)
            elif len(currents) == len(nums):
                rts.append(''.join(currents))

            currents = []

    if len(currents) > len(nums):
        rts = []
        nums = ''.join(currents)
        rts.append(nums)
    elif len(currents) == len(nums):
        rts.append(''.join(currents))
    print('{},{}'.format(''.join(rts), len(nums)))



if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            print(e)
            break