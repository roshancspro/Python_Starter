def narcissistic( value ):
    """
    A Narcissistic Number is a number which is
     the sum of its own digits, each raised to 
     the power of the number of digits in a 
     given base. In this Kata, we will restrict
      ourselves to decimal (base 10).
    """
    count = 0
    base = value
    sum = 0

    #get the total digits of number
    while base > 0:
        base = base // 10
        count += 1
    
    base = value
    #getting the sum of all digits
    #powered by count
    while base > 0:
        currVal = base % 10
        sum += pow(currVal,count)
        base = base // 10
    
    
    if(sum == value):
        return True
    
    return False

print(narcissistic(153))