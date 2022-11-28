#Kaitlyn Sourignosack
#1824497

import csv

csvreader_copy = []
pricesorted = []
price_set = []
pricesorted_wdetails = []

with open (r"PriceList.csv", 'r') as csv_price:
    contentlist = csv.reader(csv_price)
    for i in contentlist:
        pricesorted.append(i[1])
        csvreader_copy.append(i)
    price_set = set(pricesorted)

    pricesorted = []
    for a in price_set:
        pricesorted.append(a)

    #Price sorted GREATEST to LEAST
    for i in range (len (pricesorted)):
        pricesorted [i] = int (pricesorted [i])
    pricesorted.sort(reverse = True)

    for i in range (len (pricesorted)):
        pricesorted [i] = str (pricesorted[i])


    # pricesorted w details by getting the item id from csvreader_copy and into a new list
    for i in pricesorted:
        for j in csvreader_copy:
            if (j[1] == i):
                pricesorted_wdetails.append (j)


