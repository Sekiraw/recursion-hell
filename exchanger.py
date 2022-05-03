
def exchanger(arr, val, res_list):
    # simple cases
    print(val)
    if val == 0:
        return res_list
    if val == arr[-1]:
        res_list.append(arr[-1])
        return res_list
    if val < arr[-1]:
        # hungarian rounding system
        nval = 0 if val == 1 or val == 2 else 5
        if nval == 5:
            res_list.append(nval)
        return res_list

    # main
    for i in range(len(arr)):
        # rounding system (me) messes up the code a bit
        if val - arr[i] == -2:
            res_list.append(arr[i])
            val -= arr[i]
            return exchanger(arr, val+2, res_list)
        if val - arr[i] == -1:
            res_list.append(arr[i])
            val -= arr[i]
            return exchanger(arr, val+1, res_list)
        if val - arr[i] >= 0:
            res_list.append(arr[i])
            val -= arr[i]
            return exchanger(arr, val, res_list)


if __name__ == "__main__":

    money = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
    value = 14998

    ls = []
    res_list = exchanger(money, value, ls)
    print(res_list)
