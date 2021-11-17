datafile = "/Users/alexandrosbrew/Documents/ComputerScienceAlevel/FIleHandling/favourite.dat"

def showItems():
  pass


def addItem(barcode):
  f = open(datafile, "r")
  line = f.readline().strip()
  while line != '':
    if line == barcode:
      print(f'{line} is already in file')
      f.close()
      break
    else:
      f = open(datafile, "a")
      f.write(barcode)
      f.close()
      break



barcode = input("Enter the barcode: ")
addItem(barcode)