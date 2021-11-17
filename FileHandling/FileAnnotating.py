from os import error


def openFile(name,mode):
  try:
    name=name+".txt"#adds .txt to the end of the file
    myFile = open(name,mode) #opens the file and the mode that is given
    return myFile#Returns the file
  except:#If an error occurs the try and except with catch the error and prevent the code from continuing
    print("Error: ", error)
    return False

while True:
  x = input("What would you like to do? ").upper()#Makes the user input upper case.
  if x == "ADD":
    name = input("What is the name of the file you would like to open? ")
    myFile = openFile(name,"a")#opens the file that was given by the user

    if myFile:#If the file is successfully opened
      item = input("What would you like to add? ")
      myFile.write(item)#Write to the file
      myFile.write("\n")
      myFile.close()#Closes the file
    print()

  elif x == "SHOW":
    name = input("What is the name of the file you would like to display? ")
    myFile = openFile(name,"r")#Opens file that was given by the user
    
    if myFile:#Checks if the file exists and returns a bool.
      linecnt = 1
      line = myFile.readline()#Reads a single line in the file
      while line!= "":#Condition loop checks if the line that is read != an empty line
        print("Line", linecnt, ":",line.strip())#Prints the line number and what is read at the line.
        line = myFile.readline() #reads the next line
        linecnt = linecnt + 1 #adds 1 to the line count

      if linecnt==1: #checks if there is anything written in the line.
        print(name+".txt is empty")
      myFile.close()
      print()
      
  elif x == "NEW": 
    name = input("What is the name of your file? ")
    myFile = openFile(name,"w")#opens a new file in the write mode
    myFile.close()#closes file
    print()
    
  elif x=="STOP":
    break

print()
print("Thanks for coming - bye")
