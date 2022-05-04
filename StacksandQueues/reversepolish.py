import stack
numStack = stack.Stack(5)

stringInp = input("Enter your reverse polish notation: ")
for i in range(len(stringInp)):
    if stringInp[i] != "+" or int(stringInp[i]) >= 0:
        numStack.push(i)
    elif int(stringInp[i]) == "+":
        total = numStack.stack[i] + numStack.stack[i-1] 
        numStack.pop()
        numStack.pop()
        numStack.push(total)

numStack.printStack()        