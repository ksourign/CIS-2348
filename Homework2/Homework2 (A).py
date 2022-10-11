#Kaitlyn Sourignosack
#1824497

#PART A
from datetime import datetime, date

#Opening file, putting each date into list as STRINGS
datelist = []
correctformatlist = []
month = ''

date = str (input ())
while date != '-1':
    datelist.append (date)
    date = str (input ())

#For checking the dates w/ ","
def ismonthinlist(month):
    monthlist = ['January','March','April','May','June','July','August','September','October','November','December']
    if month not in monthlist:
        return False
    else:
        return True

#Finding ',' in the correct date inputs, making sure the month is spelled correctly
for listitem in datelist:
    if listitem.find (',') != -1:
        for itemindex in range(len(listitem)-1):
            if listitem[itemindex + 1] != ' ':
                month += listitem [itemindex]
            if listitem[itemindex + 1] == ' ' :
                month += listitem [itemindex]
                if ismonthinlist(month) == True:
                    correctformatlist.append(listitem)
                    month = ''
                    break

#Step 1: Checking if DATE is later than CURRENT DATE
#Step 2: Appending correct DATETIMES w/ CLOSE correct FORMAT RESULT (W/ZEROES) in another list (must convert string to dateobject)
dateobjectlist = []
currentdate = datetime.today()

for q in correctformatlist:
    dateobject = datetime.strptime(q, "%B %d, %Y")
    if (currentdate > dateobject):
        dateformat = dateobject.strftime("%m/%d/%Y")
        dateobjectlist.append (dateformat)

#dateobject in dateobjectlist converted to CORRECT RESULT format STRING without ZEROES
newformat = ''
for u in dateobjectlist:
    for t in range (len (u)):
        if (t == 0 and u[t] == '0') or (t == 3 and u[t] == '0'):
            continue
        else:
            newformat +=  u[t]
        if (t == (len(u) - 1)):
            newformat += '\n'
print (newformat)
