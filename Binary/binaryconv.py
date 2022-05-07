#Converts decimal into signed and magnitude
dennum, neg = input("Enter Denary number: "), False

if dennum[0] == "-":
    binary = bin(int(dennum[1:]))
    print("Signed and Magnitude: 1"+binary.replace("0b", ""))
else:
    binary = bin(int(dennum[0:]))
    print("Signed and Magnitude: 0"+binary.replace("0b", ""))

#Converts Decimal into 2s compliment
if dennum[0] =="-":
    pos = bin(int(dennum[1:])-1).replace("0b", "")
    flipbit = ""
    for i in pos:
        if i == "0":
            flipbit += "1"
        else:
            flipbit += "0"
    print("2s Compliment: 1"+flipbit)
else:
    pos = bin(int(dennum[0:])).replace("0b", "")
    print("2s Compliment: 0"+pos)