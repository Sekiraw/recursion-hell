import json


def kolatz(num, list):
    # print(list)
    # print(int(num))
    if num == 1:
        if 1 not in list:
            list.append(1)
        return list

    if num % 2 == 0:
        if num not in list:
            list.append(int(num))
        return kolatz(num / 2, list)
    else:
        if num not in list:
            list.append(int(num))
        return kolatz((num * 3) + 1, list)


def save_kolatz(runs):
    ls = []
    j = 0
    for i in range(runs):
        j += 1
        nls = kolatz(j, ls)

    nls.sort()
    f = open("res.txt", "w")
    f.write(str(nls))
    f.close()


def comb(kolatz_coll, list):
    if len(kolatz_coll) <= 1:
        return list
    else:
        if kolatz_coll[0+1] != kolatz_coll[0] + 1:
            list.append(kolatz_coll[1])
            nl = kolatz_coll[1:]
            return comb(nl, list)
        else:
            nl = kolatz_coll[1:]
            return comb(nl, list)


def save_comb():
    f = open("res.txt", "r")
    inp = f.read()
    nls = json.loads(inp)

    combls = []

    l = comb(nls, combls)

    f = open("combed.txt", "w")
    f.write(str(l))
    f.close()


if __name__ == "__main__":
    # kolatz
    save_kolatz(100)

    save_comb()