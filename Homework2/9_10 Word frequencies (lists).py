#Kaitlyn Sourignosack
#1824497

import csv

with open (input(),'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    list = []

    for line in csv_reader:
        for cell in line:
            list.append (cell)

countlist = []
count = 0

#solution

for u in range (len(list)):

    word = list[u]
    count = 0

    for i in range (0, len (list) ):  #looping once for 1 word, checking, and counting into list

        if (word in countlist):
            break
        if (list [i] != word):
            continue

        if (list [i] == word):
            count += 1

    else:
        countlist.append (word)
        countlist.append (count)

z=0

while z < len(countlist):

    print (countlist [z], countlist [z+1])
    z += 2




