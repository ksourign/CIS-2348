#Kaitlyn Sourignosack
#1824497

#PART C
from datetime import datetime, date

#Opening file, putting each date into list as STRINGS
datelist = []
with open ("inputDates.txt") as a:

    contents = a.readlines()
    for x in contents:
        if(x != '-1'):
            datelist.append (x.strip())

#Step 1: Checking dates in lists for COMMA FORMAT
#Step 2: For-looping the string in each element (dates) of list & checking the months w/ def ismonthinlist; if it passes the month check, it goes to correctformatlist
correctformatlist = []
month = ''

#For checking the dates w/ ","
def ismonthinlist(month):
    monthlist = ['January','February','March','April','May','June','July','August','September','October','November','December']
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

#WRITING the correct results to parsedDates.txt
with open ('parsedDates.txt', 'w') as a:
    a.write (newformat)
