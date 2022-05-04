import stack

Stack = stack.Stack(10)

def isBalanced(inp):
    if len(inp) % 2 != 0:
        return False
    
    for char in inp:
        if char == "(" or char == "{" or char == "[":
            Stack.push(char)
            print("1")
        if char == ")" or char == "}" or char == "]":
            print("2")
            if not Stack.stack:
                print("3")
                return False
            top = Stack.pop()
            print("4")
            if (top == "(" and top != ")") or (top == "{" and top != "}") or (top == "[" and top != "]"):
                print("5")
                return False
    print("6")
    return not Stack.stack

if isBalanced("{<A>(J)}"):
    print("Yes")
else:
    print("No")


