#Kaitlyn Sourignosack
#1824497

import csv
from datetime import datetime, date

contentlist_copy = []
datelist = []
dateobject_list = []
listsorteddate_wdetails = []

PastServiceDate_List = []

with open (r"ServiceDatesList.csv", 'r') as csv_servicedateslist:
    contentlist = csv.reader (csv_servicedateslist)
    for i in contentlist:
        datelist.append (i[1])
        contentlist_copy.append (i)
    # print ('datelist',datelist)


    for j in datelist:
        dateobject = datetime.strptime(j, "%m/%d/%Y")
        dateobject_list.append (dateobject)

    dateobject_list.sort ()
    # print ('dateobject list',dateobject_list)

    for i in  range (len (dateobject_list)):
        dateformat = dateobject_list[i].strftime("%m/%d/%Y")
        dateobject_list [i] = dateformat
    # print ('dateobjectlist',dateobject_list)

    #sortted dates w details
    # print ('copy content', contentlist_copy)

    for j in dateobject_list:
        dateobject1 = datetime.strptime(j,"%m/%d/%Y")
        for i in contentlist_copy:
            dateobject2 = datetime.strptime(i[1],"%m/%d/%Y")
            if dateobject1 == dateobject2:
                listsorteddate_wdetails.append (i)
            else:
                continue
    # print ('list sorted dates details',listsorteddate_wdetails)


    # for i in listsorteddate_wdetails:
    #     print(','.join(i))











