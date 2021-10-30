userbal = {
    "Alex": 10000,
    "Aidan": 100,
    "Conor": 69420,
}


class GasBill():
    def  __init__(self, standingCharge = 250, price = 50):
        self.standingCharge = standingCharge
        self.price = price
    def getName(self,):
        nameacc = input("What account do you want to use the balance from: ")
        for name in userbal:
            if nameacc in name:
                namebal = userbal[name]
                return namebal

    def getreading(self,):
        meterread = int(input("Enter the gas reading: "))
        return meterread

    def calculateUnits(self, meterread):
        lastreading = int(input("Enter the last reading: "))
        newread = meterread - lastreading
        return newread

    def calculateBalance(self, totalUnits, userbal):
        newbal = userbal - ((totalUnits * self.price) + self.standingCharge)
        return newbal

    def generateBill(self, userbal):
        print(f"The gas bill is: £{float(userbal)}, with a Standing Charge of £250.")

GasBill = GasBill()
Units = GasBill.calculateUnits(GasBill.getreading()) 
GasBill.generateBill(GasBill.calculateBalance(Units, userbal["Alex"]))
