def f(num):
    print(num)
    if num > 1:
        f(num - 1)
    else:
        print("blastoff")

f(10)