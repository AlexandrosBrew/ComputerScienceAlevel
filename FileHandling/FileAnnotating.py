from os import X_OK, error


def openFile(name,mode):
  try:
    name=name+".txt"#adds .txt to the end of the file
    myFile = open(name,mode) #opens the file and the mode that is given
    return myFile#Returns the file
  except:#If an error occurs the try and except with catch the error and prevent the code from continuing
    print("Error: ", error)
    return False

while True:
  x = input("What would you like to do? ").split() #Makes the user input upper case.
  if x[0].upper() == "ADD":
    myFile = openFile(x[1],"a") #opens the file that was given by the user
    if myFile: #If the file is successfully opened
      item = ''.join(x[2:])
      myFile.write(item)#Write to the file
      myFile.write("\n")
      myFile.close()#Closes the file
    print()

  elif x[0].upper() == "SHOW":
    myFile = openFile(x[1],"r")#Opens file that was given by the user
    
    if myFile:#Checks if the file exists and returns a bool.
      linecnt = 1
      line = myFile.readline()#Reads a single line in the file
      while len(line) != 0:#Condition loop checks if the line that is read != an empty line
        print("Line", linecnt, ":",line.strip())#Prints the line number and what is read at the line.
        line = myFile.readline() #reads the next line
        linecnt = linecnt + 1 #adds 1 to the line count

      if linecnt==1: #checks if there is anything written in the line.
        print(x[1]+".txt is empty")
      myFile.close()
      print()
      
  elif x[0].upper() == "NEW": 
    myFile = openFile(x[1],"w")#opens a new file in the write mode
    myFile.close()#closes file
    print()
    
  elif x[0].upper() =="STOP":
    break
  
  elif x[0].upper() == "COUNT":
    count = 0
    wcount = 0
    char = input("What character would you like to count? ")
    word = input("What word would you like to count?")
    myFile = openFile(x[1],"r")
    # for l in myFile.read():
    #   if char == l:
    #     count += 1
    line = myFile.readline()
    while line != "":
      if word == line:
        wcount +=1
      line = myFile.readline()
    print(count)
    print(wcount)
    myFile.close()
print()
print("Thanks for coming - bye")
