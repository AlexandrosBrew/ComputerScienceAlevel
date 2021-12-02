students = ["Oliver", "Lars", "Sophie", "Sylvia", "Bob"]

def addStudent(newname):
  students.append(newname)
  return students

def updateStudent(userinp, newname):
  for name in students:
    if userinp == name:
      students.remove(name)
      students.append(newname)
      break
    elif userinp != name:
      print("Error: the nme is not in the list.")
  return students


while True:
  menuChoice = input("Would you like to show/add/update the list? ").lower()
  if menuChoice == "add":
    userinp = input("What name would you like to add? ")
    addStudent(userinp)
    print(*students)
  elif menuChoice == "update":
    userinp = input("What name would you like to remove? ")
    newname = input("What name do you want to add? ")
    updateStudent(userinp, newname)
    print("New updated list: "+str(students))
  elif menuChoice == "show":
    print(*students)
    print(students)
		
  else:
    print("Error: that is not a command.\n")