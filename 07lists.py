#Task 1: create a list called students where each index is the first name of a student in your class (minimum 5 students)


students = ["Alex", "Neema", "Aidan", "Conor", "Mussashi"]
print('''
#######################
    Class List Menu
#######################

Type:
 - ADD to add a new student
 - SHOW to output the current class list
 - UPDATE to update an existing student
 - REMOVE to remove a student from the class list
 - EXIT to end the program
''')




while True:
  menuChoice = input("What would you like to do? ")
  

  if menuChoice.upper() == "ADD":
    nameAdd = input("What name do you want to add? ")
    students.append(nameAdd)

  elif menuChoice.upper() == "SHOW":
    print(*students)

  elif menuChoice.upper() == "UPDATE":
    selectname = input("Enter a name you want to replace: ")
    replacename = input("What do you want to replace it with? ")

    try: 
      students[students.index(selectname)] = replacename
    except ValueError:
      print("That name is not in the list.")

  elif menuChoice.upper() == "REMOVE":
    remname = input("What name do you want to remove? ")

    try: 
      students.remove(remname)
    except ValueError:
      print("That name is not in the")
  
  elif menuChoice.upper() == "EXIT":
    break