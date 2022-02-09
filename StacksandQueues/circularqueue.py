size = 4
queue = [None]*size
stindex = 0
enindex = 0


while True:
    inp = input("Would you like to push/pop/print/exit? ")
    if inp.lower() == "push":
        if stindex != size:
            val = input("What would you like to push? ")
            queue[stindex] = val
            stindex+=1
        else:
            print("Overflow")
            stindex = 0
    elif inp.lower() == "pop":
        if enindex != -1:
            queue[enindex] = None
            enindex-=1
        else:
            print("Underflow")
            enindex = size-1
    elif inp.lower() == "print":
        for i in range(size-1, -1, -1):
            print(i,":",queue[i])
        print("--------")
    elif inp.lower() == "exit":
        break