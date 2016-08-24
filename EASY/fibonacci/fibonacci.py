def fib(n):
    fiblist = [0, 1, 1]
    if n in [1, 2, 3]:
        return fiblist[n-1]
    else:
        m = 2
        while m < n:
            fiblist[0] = fiblist[1]
            fiblist[1] = fiblist[2]
            fiblist[2] = fiblist[0] + fiblist[1]
            m += 1
        return fiblist[2]


while True:
    number = int(input("Input a number: "))
    if number <= 100000:
        print(str(fib(number)))
        break
    else:
        print(str(number) + " is too large, try a number < 100,000")