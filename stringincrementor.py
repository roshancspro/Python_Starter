import re
def increment_string(strng):
    """
    write a function which increments a string,
     to create a new string. If the string 
     already ends with a number, the number 
     should be incremented by 1. If the string
      does not end with a number the number 1 
      should be appended to the new string.
    """
    index = findLastIndex(strng)
    if(index == -1):
        strng = strng + str(1)
    else:
        #Assumption that last value will be int
        try:
            val = (strng[index:])
            #print(len(val))
            intVal = int(val) + 1
        except ValueError:
            return strng +str(1)
        
        diff = len(val) - len(str(intVal))
        if(diff > 0):
            val = '0'*diff + str(intVal)
        else:
            val = str(intVal)

        strng = strng[:index] +val
    
    #print(strng)
    return strng

def findLastIndex(strng):
    """
    returns the last index of integer
    in the given string

    foo1a2 - returns 5
    foo1 - returns 3
    foo - returns -1
    """

    p = re.compile("\\d+")
    iter = re.finditer(p, strng)
    indices = [m.start(0) for m in iter]
    #Handle case for no number 
    # in string
    try:
        return indices[-1]
    except IndexError:
        #print("No Number found")
        return -1

#findLastIndex("foo")
#findLastIndex("foo1")
#findLastIndex("foo1a2")

print(increment_string("U9651767980@5"))
print(increment_string("U9651767980@"))
print(increment_string("U9651767980"))
print(increment_string("U000"))
print(increment_string("U001"))
print(increment_string("U099"))