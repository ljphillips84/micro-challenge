def is_palindrome(istring):
        '''Takes a string as input and returns a boolean
       (True/False) output dependant on whether the
       string is a palindrome.
    '''
    for i in xrange(len(istring)/2):
        if istring[i] != istring[-(i+1)]:
            return False
    return True
