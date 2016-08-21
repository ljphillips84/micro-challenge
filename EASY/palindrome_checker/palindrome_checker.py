import sys

def is_palindrome(istring):
    '''Takes a string as input and returns a boolean
       (True/False) output dependant on whether the
       string is a palindrome.
    '''
    for i in range(int(len(istring)/2)):
        if istring[i] != istring[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    print(is_palindrome(sys.argv[1]))
    
