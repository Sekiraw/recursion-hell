
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)


def eq(list1, list2):
    print(list1, list2)

    if len(list1) != len(list2):
        print("The lists are not equal")
        return False

    # if we get an empty list we are fine
    if len(list1) == 0 and len(list2) == 0:
        return True

    if list1[0] * 2 == list2[0]:
        # splitting to head and tail
        new_list1 = list1[1:]
        new_list2 = list2[1:]
        return eq(new_list1, new_list2)
    else:
        print("error at", list1[0], list2[0])
        return False


# not recursion
def add_two(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return 0

    list1.reverse()
    list2.reverse()

    list1_digits_as_string = ""
    list2_digits_as_string = ""
    res = 0

    for i in range(len(list1) if len(list1) >= len(list2) else len(list2)):

        list1_digits_as_string += str(list1[i] if list1[i] else 0)
        list2_digits_as_string += str(list2[i] if list2[i] else 0)

        res = int(list1_digits_as_string) + int(list2_digits_as_string)
        # print(int(string), int(string2))

    return res


# it's ugly as s, but I don't know how to make it more efficient
def roman_to_int(str, res=0):
    print(str)
    print(res)

    # on empty stack return the result
    if str == "":
        return res

    if str[0] == "I":
        if len(str) > 1:
            if str[1] == "V":
                return roman_to_int(str[2:], res+4)
            if str[1] == "X":
                return roman_to_int(str[2:], res + 9)
        return roman_to_int(str[1:], res + 1)

    if str[0] == "V":
        return roman_to_int(str[1:], res + 5)
    if str[0] == "X":
        if len(str) > 1:
            if str[1] == "L":
                return roman_to_int(str[2:], res+40)
            if str[1] == "C":
                return roman_to_int(str[2:], res + 90)
        return roman_to_int(str[1:], res+10)
    if str[0] == "L":
        return roman_to_int(str[1:], res+50)
    if str[0] == "C":
        if len(str) > 1:
            if str[1] == "D":
                return roman_to_int(str[2:], res+400)
            if str[1] == "M":
                return roman_to_int(str[2:], res + 900)
        return roman_to_int(str[1:], res+100)
    if str[0] == "D":
        return roman_to_int(str[1:], res+500)
    if str[0] == "M":
        return roman_to_int(str[1:], res+1000)


def median_of_two(list1, list2, res_list):
    print(res_list)

    # simple case
    if len(list1) == 0 and len(list2) == 0:
        # return res_list
        if len(res_list) % 2 == 0:
            med = len(res_list) / 2
            return (res_list[int(med)] + res_list[int(med)-1]) / 2
        else:
            med = (len(res_list) - 1) / 2
            return res_list[int(med)]

    n = len(list1)
    m = len(list2)

    if n and m > 0:
        if list2[0] > list1[0]:
            res_list.append(list1[0])
            nl = list1[1:]
            return median_of_two(nl, list2, res_list)
        if list1[0] > list2[0]:
            res_list.append(list2[0])
            nl = list2[1:]
            return median_of_two(list1, nl, res_list)
        if list1[0] == list2[0]:
            res_list.append(list1[0])
            nl = list1[1:]
            return median_of_two(nl, list2, res_list)
    elif n == 0 and m != 0:
        res_list.append(list2[0])
        nl = list2[1:]
        return median_of_two(list1, nl, res_list)
    elif m == 0 and n != 0:
        res_list.append(list1[0])
        nl = list1[1:]
        return median_of_two(nl, list2, res_list)


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


def search_insert(list, index):
    for i in range(len(list)):
        if list[i] == index:
            return i
    list.append(index)
    list.sort()
    for i in range(len(list)):
        if list[i] == index:
            return i


if __name__ == "__main__":
    # print(fact(6))

    # equality between 2 lists
    # it should return true if the second list contains the first list's elements but at the power of 2
    # print(eq([1, 2, 5, 6], [2, 4, 10, 12]))

    # add two numbers (medium)
    # You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
    # reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum
    # as a linked list.
    # You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    # <-- I assume that the basic lists are sorted -->
    # print(add_two([2, 4, 3], [5, 6, 4]))

    # roman to integer
    # with empty stack
    # roman_to_int("MCMXCIV")

    # Median of Two Sorted Arrays (hard)
    # ls = []
    # print(median_of_two([1, 3, 5, 7, 9], [2, 6, 7, 8, 9], ls))

    # kolatz
    # j = 10
    # for i in range(1000):
    #     j += 1
    #     nls = kolatz(j, [])
    #
    # nls.sort()
    # print(nls) # getting the numbers that it has gone through cuz why not

    # Search Insert Position
    # Given a sorted array of distinct integers and a target value, return the index if the target is found.
    # If not, return the index where it would be if it were inserted in order.
    print(search_insert([1, 3, 4, 5, 6], 5))
