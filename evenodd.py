def check(x):
    if x % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    a = int(input("Enter a Number: "))
    res = check(a)
    print(res)

