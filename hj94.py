#encoding: utf-8

def solution():
    input()
    names = input().split()
    input()
    tickets = input().split()
    stats = dict.fromkeys(names, 0)
    Invalid = 0
    for ticket in tickets:
        if ticket in stats:
            stats[ticket] += 1
        else:
            Invalid += 1

    for name in names:
        print('{} : {}'.format(name, stats.get(name, 0)))

    print('Invalid : {}'.format(Invalid))



if __name__ == '__main__':
    while True:
        try:
            solution()
        except Exception as e:
            import traceback
            traceback.print_exc()
            break