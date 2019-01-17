import heapq
def queue_time(customers, n):
    """
    There is a queue for the self-checkout 
    tills at the supermarket. Your task is 
    write a function to calculate the total 
    time required for all the customers to 
    check out!

    The function has two input variables:

    customers: an array (list in python) of 
    positive integers representing the queue. 
    Each integer represents a customer, and its 
    value is the amount of time they require 
    to check out.

    n: a positive integer, the number of 
    checkout tills.
    
    The function should return an integer, the total time required.
    """

    if(customers == None or len(customers) == 0):
        return 0
    totalCustomers = len(customers)
    
    if(n == 1):
        return sum(customers)
    
    if(totalCustomers < n):
        return max(customers)
    
    heapList = customers[:n]
    # using heapify to convert list into heap 
    heapq.heapify(heapList) 
    
    total = len(customers)
    
    for i in range(n, total):
        val = heapq.heappop(heapList)
        val = val + customers[i]        
        heapq.heappush(heapList,val)
    
    #Removing final items from heap
    for i in range(n):
        val = heapq.heappop(heapList)
    #print(val)
    return val
    
print(queue_time([1,2,3,4,5],1))
print(queue_time([],1))
print(queue_time([1,2,3,4,5], 100))
print(queue_time([2,2,3,3,4,4], 2))
print(queue_time([10,2,3,3], 2))
print(queue_time([2,3,10],2))