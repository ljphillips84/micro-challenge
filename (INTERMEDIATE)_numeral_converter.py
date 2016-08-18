'''
Converts roman numerals into ints and back, uses recursive solving by default
however, this can be solved iteratively as well.
'''

#Required information for converting roman numerals into int
lookuptable = [("M", 1000),
               ("CM", 900),
               ("D", 500),
               ("CD", 400),
               ("C", 100),
               ("L", 50),
               ("X", 10),
               ("IX", 9),
               ("V", 5),
               ("IV", 4),
               ("I", 1)]

def convert_to_roman (number, output=""):
    '''Takes a number as an int, and returns a string of roman numerals
       with the same value.
    '''
    return

def convert_to_english (romanstring, outnum=0):
    '''Takes a string of roman numerals, and returns an integer with
       the same value
    '''
    return

print convert_to_roman(3459)
print convert_to_english("MMMCDLIX")
