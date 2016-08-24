from random import randint

def random_list(N):
    random_list = [randint(0,1000000)]
    n = 1
    while n < N:
        random_list.append(randint(0,1000000))
        n += 1
    return random_list

def is_prime(p):
    is_prime_check = True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            is_prime_check = False
    return is_prime_check

# def is_prime2(p):
#     return 2 in [p,2**p%p]

def find_max_prime(rList):
    max_prime = 0
    for number in rList:
        if is_prime(number):
            if number > max_prime:
                max_prime = number
    return max_prime

list = random_list(int(input("Number: ")))
testlist = [17,24,59]

# for number in list:
#     if is_prime(number) != is_prime2(number):
#         print(number,is_prime(number),is_prime2(number))

print("Max Prime: ",str(find_max_prime(list)))