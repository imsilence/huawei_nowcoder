#encoding: utf-8

def handle(nums, diff):
    flags = [0] * len(nums)
    def incr():
        for i in range(len(flags)):
            if flags[i] == 0:
                flags[i] = 1
                break
            else:
                flags[i] = 0

    flag = lambda x : 1 if x > 0 else -1
    while sum(flags) != len(nums):
        if sum([flag(flags[i]) * nums[i] for i in range(len(nums))]) == diff:
            print(flags)
            return True
        incr()

    return False

def solution():
    input()
    nums = map(int, input().split())
    categorys = [[], [], []]
    for num in nums:
        if num % 5 == 0:
            categorys[0].append(num)
        elif num % 3 == 0:
            categorys[1].append(num)
        else:
            categorys[2].append(num)

    diff = sum(categorys[0]) - sum(categorys[1])
    if handle(categorys[2], diff):
        print(categorys)
        print("true")
    else:
        print("false")




if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break