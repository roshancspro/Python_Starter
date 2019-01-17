def row_sum_odd_numbers(n):
    #your code here
    if(n == 1):
        return 1
    startIndex = ((n-1) * (n))//2
    startVal = (startIndex * 2) + 1
    sum = 0

    while(n > 0):
        print(startVal)
        sum += startVal
        n -= 1
        startVal += 2
    
    print(sum)
    return sum


row_sum_odd_numbers(5)


