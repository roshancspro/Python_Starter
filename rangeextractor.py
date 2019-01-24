def solution(args):
    """
    A format for expressing an ordered list of 
    integers is to use a comma separated list 
    of either

    1. individual integers or
    or a range of integers denoted by the 
    starting integer separated from the end 
    integer in the range by a dash, '-'. 
    The range includes all integers in the 
    interval including both endpoints. 
    It is not considered a range unless it 
    spans at least 3 numbers. 
    For example ("12, 13, 15-17")
    """
    if not args:
        return
    
    argsLen = len(args)

    if(argsLen <= 2):
        return args

    prevVal = args[0]
    #print(args)

    rangeNums = ""
    prevCount = 0

    for num in range(1,argsLen):
        if(args[num] - prevVal == 1):
            prevCount += 1
        else:
            rangeNums += updateRangeVal(prevVal,prevCount)+","
            prevCount = 0
        prevVal = args[num]
    
    rangeNums +=updateRangeVal(prevVal,prevCount)
    
    return rangeNums

def calcRangeVal(val, diff):
    rangeStart = val - diff
    return rangeStart, val


def updateRangeVal(val, diff):
    if(diff > 1):
        start,end = calcRangeVal(val,diff)
        return (str(start)+"-"+str(end)) 
    elif(diff == 1):
        return (str(val-1)) + ","+str(val)

    elif(diff == 0):
        return str(val)

    

#Consecutive number
print(solution([1,2,3,4]))
#conbination of 2 successive num and more than 2 
print(solution([1,2,4,5,6,7,9]))
#Sample test case
print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
#solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])





