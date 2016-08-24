def is_palindrome(istring):
    check = True
    for l in range(int(len(istring)/2)):
        if istring[l].lower() != istring[-(l+1)].lower():
            check = False
    return check

if is_palindrome(input("Input your word:")):
    print("PALINDROME!")
else:
    print("not palindrome...")
