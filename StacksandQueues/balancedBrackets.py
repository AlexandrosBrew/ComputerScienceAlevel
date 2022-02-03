import stack

Stack = stack.Stack(10)

def isBalanced(inp):
    if len(inp) % 2 != 0:
        return False
    
    for char in inp:
        if char == "(" or char == "{" or char == "[":
            Stack.push(char)
        if char == ")" or char == "}" or char == "]":
            if not Stack.stack:
                return False
            top = Stack.pop()
            if (top == "(" and top != ")") or (top == "{" and top != "}") or (top == "[" and top != "]"):
                return False
    return not Stack.stack

if isBalanced("{<A>(J)}"):
    print("Yes")
else:
    print("No")


