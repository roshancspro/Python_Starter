def capitalize(s):
    """
    Given a string, capitalize the letters
    that occupy even indexes and odd indexes 
    separately, and return as shown below. 
    Index 0 will be considered even.
    """
    capsList = []
    counter = 0
    evenVersion = ''
    oddVersion = ''
    for str in s:
        if(counter % 2 == 0):
            evenVersion += str.upper()
            oddVersion += str
        else:
            oddVersion += str.upper()
            evenVersion += str
        
        counter += 1
    
    capsList.append(evenVersion)
    capsList.append(oddVersion)

    return capsList

print(capitalize("abcdef"))    
          



