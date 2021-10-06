#Assigning varibales means the "=" sign is invovled. E.g:
name = "alex"

#We input using the input() command, and we output using the print() command. E.g:
userinput = input("This is the input command. ")
print("This outputs what ever is inside here.")

#Casting is when you change the data type of a variable. E.g: printing x would throw an error as you cant contatinate an integer.
#To fix this you use the str() command
x = 4
print("You scored "+str(x))

#You can handle strings by using a series of methods such as:
string = "Hello how are you?"
print(string.split())#split each word.
print(string.upper())#makes everything uppercase.
print(string.lower())#makes everything lowercase.
print(string.capitalize)#capitalizes the string

#You can access individual characters by using loops.
listchar = []
for characters in string:
    listchar.append(characters)
print(listchar)

#if is used to begin an if statement, elif is to continue the statement with a condition, else is used if there is no use for a condition.
if x > 4:
    print("Bigger than 4")
elif x < 4:
    print("Smaller than 4")
else:
    print("It is 4")

#For loops are used when a loop needs to end in a range. E.g:
for i in range(0, 5):#Stops when 5 loops are done.
    print(i)

#While loops are used when a loop should end if a condition is met. E.g
while x != 7:
    print(x)
    x+=1

#Subroutines are used to be able to call on prewritten code later in the code.

mylist = ["Hello"]
def addToList(userinp):
    mylist.append(userinp)
    return mylist

userinp = input("Add to list: ")
addToList(userinp)
print(mylist)