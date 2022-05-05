
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


if __name__ == "__main__":
    # print(fact(6))

    # equality between 2 lists
    # it should return true if the second list contains the first list's elements but at the power of 2
    print(eq([1, 2, 5, 6], [2, 4, 10, 12]))