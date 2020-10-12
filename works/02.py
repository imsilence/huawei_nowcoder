#encoding: utf-8
import sys

def pay(price, plan, actual):
    # 总消费
    total = 0

    # 每天支付费用, 额外外支付费用
    dayPay, limitPay = 0, 0

    dayLimit = 15 #额外限期

    if price >= 100: # >=100元费用
        dayPay, limitPay = 5, 3
    elif price >= 50: # >=50元费用
        dayPay, limitPay = 3, 2
    else:   # < 50 元费用
        dayPay = 1

    if actual <= dayLimit:
        total += actual * dayPay # 额外限期内
    else: # 额外限期
        total += dayLimit * dayPay + (actual - dayLimit) * limitPay

    # 超过预还期
    if actual > plan:
        total += actual - plan

    # 消费在本书价格内
    if total > price:
        total = price

    return total


def solution():
    total = 300
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            break
        # 处理每行数据, 单价, 计划天数，实际天数
        price, plan, actual = list(map(int, line.split(',')))
        payTotal = pay(price, plan, actual)
        # 针对条件2 当不足支付时, 需要计算最多借阅时间和价格
        # 在pay中将价格分为三段时间，0-超额期, 超额期-计划期，计划期-实际期
        total -= payTotal
    print(total)

if __name__ == '__main__':
    solution()