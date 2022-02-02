class Stack:
    def __init__(self, size):
        self.size = size
        self.index = 0
        self.stack = [None]*size

    def push(self, data):
        if self.index != self.size:
            self.stack[self.index] = data
            self.index += 1
        else:
            print("Stack Overflow")
    
    def pop(self):
        if self.index != 0:
            self.stack[self.index-1] = None
            return self.stack
        else:
            print("Stack underflow")
    
    def printStack(self):
        for i in range(self.size-1, self.index, -1):
            print(i, ":")
        for i in range(self.index-1, -1, -1):
            print(i, ":", self.stack[i])
        print("--------")

if __name__ == "__main__":
    stack = Stack(10)
    while True:
        inp = input("0. Pop\n1. Push\n2. Print stack\n3. Exit\n")
        if inp == "0":
            stack.pop()
        if inp == "1":
            data = input("What do you want to push? ")
            stack.push(data)
        if inp == "2":
            stack.printStack()
        if inp == "3":
            break



