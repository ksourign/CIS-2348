#Kaitlyn Sourignosack
#1824497

listfrominput = []
splitlist = []
listfrominput.append (input())

for i in listfrominput:
    a = i.split (' ')
    splitlist = i.split (' ')

countlist = []

for u in range (len(splitlist)):

    word = splitlist[u]
    count = 0

    for i in range (0, len (splitlist) ):

        if (splitlist [i] != word):
            continue

        if (splitlist [i] == word):
            count += 1

    else:
        countlist.append (word)
        countlist.append (count)

z=0

while z < len(countlist):

    print (countlist [z], countlist [z+1])
    z += 2