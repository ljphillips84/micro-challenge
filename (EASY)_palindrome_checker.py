def is_palindrome(istring):
    for i in xrange(len(istring)/2):
        if istring[i] != istring[-(i+1)]:
            return False
    return True
