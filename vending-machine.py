
def machine(m_type, stock, change, res):
    # simple cases
    if change < 0:
        print("error - you have to give more money")
        return None

    if change == 0 or change == 1 or change == 2:
        return res
    elif change == 3 or change == 4:
        if stock[-1] > 0:
            res.append(5)
            return res
        else:
            print("error - out of stock")
            return None

    # main
    for i in range(len(money_types)):
        if change - m_type[i] >= 0 and stock[i] > 0:
            change -= m_type[i]
            res.append(m_type[i])
            stock[i] -= 1
            return machine(m_type, stock, change, res)


if __name__ == "__main__":
    # base
    money_types = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
    money_stock = [2,     10,    10,   10,   10,   10,  10,  10,  0,  2, 10, 10]
    res = []

    to_be_paid = 2022
    money_paid = 20000
    change = money_paid - to_be_paid
    print(change, "has to be paid")

    money = machine(money_types, money_stock, change, res)
    print(money, "change the machine gives")