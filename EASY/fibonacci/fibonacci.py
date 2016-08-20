def fib(n):
    try: 
        n = int(n) # if input is not an integer then trhow exception
        if n > 100000: # if input too big then return error msg
            return "Input too big"
        else: #fibonnacci loop
            a, b = 1, 1 # first 2 fibonacci numbers
            for _ in range(n-1):
                a, b = b, a + b
            return a
    except:
        return "Input must be an integer"


if __name__ == "__main__":
    val = input("Input an integer < 100,000: ")
    print('n = {0}: F(n) = {1}'.format(val, fib(val)))

