"""
Create a simple calculator that given 
a string of operators (+ - * and /) and 
numbers separated by spaces returns the 
value of that expression
"""

#this is dictionary which specifies
#all valid calculator option and 
#there priority - 1 is top priority.
prioritySym ={'+':2,'-':2,"*":1,'/':1}

class Calculator(object):
    
    def __init__(self):
        #Stack for storing numbers
        self.numStack = []
        #Stack for storing operators
        self.operatorStack = []

    def evaluate(self, string):
        allValues = string.split(" ")
        #implies no spaces added
        if(len(allValues) == 1):
            try:
                val = int(allValues[0])
                return val
            except ValueError:
                print("spaces needed between numbers and ops")
                return 

        for val in allValues:
                
            if(val in prioritySym):
                #if priority of operator is less 
                #than incoming operator, push 
                #operator in stack else perform
                #operation of current operation 
                #and append the result with 
                #current operator.
                while self.operatorStack and prioritySym[self.operatorStack[-1]] <= prioritySym.get(val):
                        calculateResult(self.operatorStack,self.numStack)
                
                self.operatorStack.append(val)
            else:
                self.numStack.append(val)

        while self.operatorStack:
            calculateResult(self.operatorStack,self.numStack)
    
        return self.numStack.pop()

def calculateResult(opStack, numStack):
    if numStack and opStack:
        val1 = float(numStack.pop())
        val2 = float(numStack.pop())
        op = opStack.pop()
        if(op == '+'):
            result = val1 + val2
        elif(op == '-'):
            result = val2 - val1
        elif(op == '*'):
            result = val1 * val2
        elif(op == '/'):
            result = val2 // val1
        
        numStack.append(result)
        



if __name__ == "__main__":
    """
    calc = Calculator()
    print(calc.evaluate("4 + 5"))
    calc = Calculator()
    print(calc.evaluate("5 - 4"))
    calc = Calculator()
    print(calc.evaluate("4 - 5"))
    calc = Calculator()
    print(calc.evaluate("4 / 2"))
    calc = Calculator()
    print(calc.evaluate("2 / 4"))
    calc = Calculator()

    print(calc.evaluate("2"))
    calc = Calculator()

    print(calc.evaluate("2+"))
    calc = Calculator()

    print(calc.evaluate("4 + 5 + 3"))
    calc = Calculator()
    print(calc.evaluate("4 + 5 * 3"))
    calc = Calculator()
    print(calc.evaluate("4 * 5 * 3"))
    """
    #calc = Calculator()
    #print(calc.evaluate("4 * 5 + 3"))
    calc = Calculator()
    print(calc.evaluate("2 / 2 + 3 * 4 - 6"))
    calc = Calculator()
    print(calc.evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
    calc = Calculator()
    print(calc.evaluate("2.2 + 3"))
    
    


