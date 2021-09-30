'''
Write a program that asks the user for a price of an item.  Include a function that returns the VAT for the item.  This should be output in the main program.'''


def vatCalculator(price):
  #add the code below to calculate the price including 10% VAT
  vatPrice = userinp * 1.2
  return vatPrice

#add the code below to ask the user for the price of an item and stores as a float
userinp = int(input("Enter the price of the item (with 20% VAT): "))

price = vatCalculator(userinp)

print("£"+price)



#extension - validate price so only numbers greater than 0 can be entered. With a maximum of 2 decimal places. 