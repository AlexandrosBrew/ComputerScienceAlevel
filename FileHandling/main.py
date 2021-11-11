datafile = "/Users/alexandrosbrew/Documents/ComputerScienceAlevel/FIleHandling/favourite.dat"

def showItems():
  pass


def addItem(barcode):
  f = open(datafile, "r")
  line = f.readline().strip()
  while line != '':
    if line == barcode:
      print(f'{line} is already in file')
    else:
      f = open(datafile, "a")

  f.close()

barcode = input("Enter the barcode: ")
addItem(barcode)