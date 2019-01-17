def validBraces(string):
    """
    function that takes a string of braces, 
    and determines if the order of the braces 
    is valid. It should return true if the 
    string is valid, and false if it's invalid.
    """
    stack = []
    start_symbol = ["(","{","["]
    symbol ={"(":")","{":"}","[":"]"}
    for str in string:
        if(str in start_symbol):
            stack.append(str)
        else:
        #if list is empty
            if(len(stack) == 0):
                return False
            
            matchingSym = stack.pop()
            if(symbol.get(matchingSym) != str):
                return False
    if(len(stack) != 0):
        return False
    
    return True

print(validBraces("()"))