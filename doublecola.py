import math
def whoIsNext(names, r):
    if(names == None):
        return
    
    if(r == None or r == 0):
        return

    total = len(names)
    
    if(r <= total):
        return names[r-1]
    
    #Geometric Sequence find nth repetition logic
    currVal = r // total
    # 2 is geometric difference
    nVal = math.floor(math.log(currVal,2))
    try:    
        #print(nVal)
        twoPowVal = pow(2,nVal)
        #total is starting value 
        sum = total * ((1 - twoPowVal)//(1-2))
        #getting index of next value
        # Assumption is diff will never
        
        diffquo = (r - sum)//twoPowVal
        #print("quo",diffquo)
        diffrem = (r - sum)%twoPowVal
        #print("rem",diffrem)
        if(diffrem > 0):
            diffrem = 1

        indexVal = (diffquo+diffrem)%total
        #print("index",indexVal)
        return names[indexVal-1]
    except IndexError:
        return names[0]
    

print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1))
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52))
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951))