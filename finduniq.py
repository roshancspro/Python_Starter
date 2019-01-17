def find_uniq(arr):
    """
    There is an array with some numbers. 
    All numbers are equal except for one.
    return the different number
    assumtion: array size will be atleast 3.
    """
    length = len(arr)

    if(length < 3):
        print("array length should be atleast 3")
        return
    
    sameVal = getSameVal(arr)

    for i in range(0, length):
        if(sameVal != arr[i]):
            return arr[i]
  

def getSameVal(arr):
    """
    checks for same repeating number in 
    array of format [1,1,1,1,1,21,1,1]
    and return the same repeating number

    assumption: array size should be atleast 
    3.
    """
    currentVal = 0 
    for i in range(1,3):
        #scenario when first element is not different one
        if(arr[currentVal] == arr[i]):
            return arr[i]

        #scenario when first element is different one
        return arr[1]
        

  