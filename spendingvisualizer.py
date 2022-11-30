import datetime as dt #for sorting receipts by date
import matplotlib.pyplot as plt # for plot

class Receipt:
    def __init__(self, date, shopName, cost):
        self.date = date
        self.shop = shopName
        self.cost = cost #in pence
    def toString(self):
        return self.date + " " + self.shop + " " + str(self.cost)


def loadReceiptsFromFile(filename):
    receipts = []
    with open(filename) as file:
        print("file opened")
        for line in file:
            line = line.split()
            date = line[0]
            costSplit = line[1].split(".")
            cost = int(costSplit[0])*100 + int(costSplit[1])
            receipt = Receipt(date, "shop", cost)
            receipts.append(receipt)
        return receipts


receipts = loadReceiptsFromFile("lidl.txt")
receipts.sort(key=lambda x: dt.datetime.strptime(x.date, '%d.%m.%Y')) #sorting receipts by date
for receipt in receipts:
    print(receipt.toString())

plt.title("Money spent in Liverpool", fontsize=20)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Money spent (GBP)", fontsize=20)
plt.grid()



plt.show()
plt.savefig('spendings.png')

print("You reached the program's end")
