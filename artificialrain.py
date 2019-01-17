def artificial_rain(garden):
    """
    Little Petya often visits his grandmother 
    in the countryside. The grandmother has a 
    large vertical garden, which can be 
    represented as a set of n rectangles of 
    varying height. Due to the newest 
    irrigation system we can create artificial 
    rain above them.
    Creating artificial rain is an expensive 
    operation. That's why we limit ourselves 
    to creating the artificial rain only above
     one section. The water will then flow to 
     the neighbouring sections but only if each 
     of their heights does not exceed the height 
     of the previous watered section.
    """
    
    flowList = []
    if(garden == None or len(garden) == 0):
        return 0

    gardenLen = len(garden)

    if(gardenLen == 1):
        return 1
    
    counter = 1

    #initializing flow list
    a = Flow(0,0)
    flowList.append(a)

    
    #calculating the left flow
    while( counter < gardenLen):
    
        try:
            if(garden[counter-1] <= garden[counter]):
                leftVal = flowList[counter-1].left
                a = Flow(leftVal+1,0)
                flowList.append(a)
            else:
                a = Flow(0,0)
                flowList.append(a)

        except IndexError:
            print("got the exception")
        
        counter +=1

    
    #calculating the right flow
    #starting counter cursor from second last
    counter = gardenLen - 2 

    while counter >= 0:
        if(garden[counter+1] <= garden[counter]):
                
                rightVal = flowList[counter+1].right
                a = flowList[counter]
                a.right = rightVal + 1
                flowList[counter] = a
                #flowList.append(a)

        counter -= 1
    
    maxVal = 0

    for flow in flowList:
        #extra 1 for current garden
        totalFlowVal = flow.totalFlow()
        if(totalFlowVal > maxVal):
            maxVal = totalFlowVal

    return maxVal

class Flow:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.left)+" "+str(self.right)
    
    def totalFlow(self):
        #added 1 for current Rectangle
        return self.right+self.left+1

if __name__ == "__main__":
    print(artificial_rain([1, 2, 1, 2, 1]))