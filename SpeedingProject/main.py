data = [[2, True], [3, False], [4, True], [1, False], [3, True], [4, False], [8, False], [5, True], [6, False], [8, False],[5, True]]

def getInput():
    ageInput = 0
    while ageInput == 0:
        try: 
            ageInput = int(input("Enter age: "))
        except:
            print("Enter a valid input.")
    if ageInput == 999:
        return False
    speedInput = 0
    while speedInput == 0:
        try:
            speedInput = int(input("Enter Speeding: "))
        except:
            print("Value entered is invalid.")
    if speedInput == 999:
        return False
    return [ageInput, speedInput]


def displayPercent(data):
    speedingcount = 0
    for i in range(len(data)):
        if data[i][1] == True:
            speedingcount +=1
    percent = speedingcount/len(data) *100
    return int(percent)

#print("Percent of people speeding = "+str(displayPercent(data))+"%")
userinp = getInput()
if userinp == False:
    print("Input Finished.")
else:
    getInput()
