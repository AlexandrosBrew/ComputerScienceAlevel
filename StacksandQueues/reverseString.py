import string
import stack

stringStack = stack.Stack(10)

inp = str(input("Enter your string:"))
for i in range(len(inp)):
    stringStack.push(inp[i])
    stringStack.printStack()

for i in range(len(inp)):
    stringStack.pop()
    stringStack.printStack()
