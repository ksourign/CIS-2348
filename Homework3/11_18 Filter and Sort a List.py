#Kaitlyn Sourignosack
#1824497

list = []
numberlist = []
finallist = []
splitlist = []

list.append (input())

for i in list:
    splitlist = i.split (' ')


for i in splitlist:
    integer = int (i)
    numberlist.append (integer)

for i in numberlist:
    if i >= 0:
        finallist.append (i)

finallist.sort()

for i in finallist:
    print (i,'', end = '')


