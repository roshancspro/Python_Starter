def race(v1, v2, g):
    """
    given two speeds v1 (A's speed, 
    integer > 0) and 
    v2 (B's speed, integer > 0) and a lead 
    g (integer > 0) how long will it 
    take B to catch A?
    """
    #if speeds are negative, stop
    if(v1 < 0 or v2 < 0):
        print("neither speed can be negative")
        return
    
    if(g < 0):
        print("lead cannot be a negative value")
        return
    
    if(v1 >= v2):
        print("v1 speed"+v1+"should be less than v2"+v2)
        return None
    
    diffInSpeed = v2 - v1
    diffInSpeedPerSec = diffInSpeed / (60 * 60)
    totalTimeToCoverinSec = g/diffInSpeedPerSec
    #calculate minute and second first
    minute,sec = getFormattedTime(totalTimeToCoverinSec)
    hr,minute = getFormattedTime(minute)

    print(hr)
    print(minute)
    print(int(sec))

    return [int(hr),int(minute),int(sec)]


def getFormattedTime(time):
    return time/60,time%60 

#race(80,91,37)
race(80,100,40)
    


