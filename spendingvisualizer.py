import datetime as dt #for sorting receipts by date
import matplotlib.pyplot as plt # for plot
import datetime as dt   # to convert STRINGS to DATETIME DATES
import matplotlib.dates as mdates # to convert DATETIME DATES to MATPLOTLIB DATES so there is equal space between them on the plot

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
for receipt in receipts:    #debug: check if loaded properly
    print(receipt.toString())

dates = [receipt.date for receipt in receipts]      #extracting the list of dates (for the plot)
prices = [receipt.cost/100 for receipt in receipts] #extracting the list of prices (for the plot) WITH converting FROM pence TO pounds
#prices_join_days = []
#for price in prices


fig, ax = plt.subplots() #for access to labels

## cosmetics ##
plt.title("Money spent in Liverpool", fontsize=20)
plt.xlabel("Date", fontsize=20)
plt.ylabel("Money spent (GBP)", fontsize=20)
plt.grid()

dates_as_datetime = [dt.datetime.strptime(date,'%d.%m.%Y').date() for date in dates]
dates_as_mdates = mdates.date2num(list(dates_as_datetime))  #convert dates from DATETIME DATE to MATPLOTLIB DATE format in order to visualise them with equal space between
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))   #to make dates working
plt.gca().xaxis.set_major_locator(mdates.DayLocator())                  #to make dates working

plt.plot(dates_as_mdates, prices, marker = 'o', label = "Shoppings", color = 'r', linestyle = '')  #creation of the actual plot


plt.gcf().autofmt_xdate() #format the date labels to more readable

plt.legend(loc="upper left", prop={'size': 20})
ax.yaxis.set_major_formatter('£{x:1.2f}')   #format the cost labels as £

every_nth = 4   #show only some of the dates to make it not too messy - might want to modify it so that it depends on the range of date
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)

plt.savefig('spendings.png')
plt.show()

print("You reached the program's end")

# To do:
# trendline
# qt interface maybe