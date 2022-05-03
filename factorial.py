
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)


if __name__ == "__main__":
    print(fact(6))