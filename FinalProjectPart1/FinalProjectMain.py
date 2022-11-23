#Kaitlyn Sourignosack
#1824497

import csv
from datetime import datetime, date
from FinalProjectPastServiceDateInventory import listsorteddate_wdetails
from FinalProjectPrice import pricesorted_wdetails

#lists for finding full inventory
FullInventory_List = []
manufacturersorted = []
manufacturersorted_wdetails = []
csvreader_copy = []


#lists for finding past service date
PastServiceDate_List = []

#lists for finding damaged inventory
mostexpensive_to_least_list = []
damaged_inventory_list = []


#lists for Item type inventory list
diff_inv_types = []



with open (r"ManufacturerList.csv", 'r') as csv_manufacturerfile:
    contentlist = csv.reader(csv_manufacturerfile)
    for i in contentlist:
        manufacturersorted.append(i[1])
        csvreader_copy.append (i)
    manufac_set = set(manufacturersorted)
    # print ('manufac set',manufac_set)
#manufac_set remove duplicates




#SORTS A-Z in manufac_set IN manufacturersorted
    manufacturersorted = []
    for a in manufac_set:
        manufacturersorted.append (a)
    manufacturersorted.sort()
    # print ('manufacturersorted',manufacturersorted)





#manufacturesorted_wdetails include other details of the sorted manufacturers
    for i in manufacturersorted:
        for j in csvreader_copy:
            if (j[1] == i):
                manufacturersorted_wdetails.append (j)
    # print ('manufacturersorted w details',manufacturersorted_wdetails)




#adding PRICE to correct id in manufacturer sorted w details
    for j in pricesorted_wdetails:
        for i in manufacturersorted_wdetails:
            if i[0] == j[0]:
                i.insert (3, j[1])
    # print ()
    # print ('manufacturer sorted w details and PRICE',manufacturersorted_wdetails)



#adding DATES to correct id in manufacturersorted w details
    for j in listsorteddate_wdetails:
        for i in manufacturersorted_wdetails:
            if i[0] == j[0]:
                j.insert (1,i[1])
                j.insert (2,i[2])
                j.insert (3,i[3])
                j.insert (5,i[4])
    # print ()
    # print ('list sorted w details and DATES',listsorteddate_wdetails)



#######################################





#PART A
#OUTSIDE OF GIVEN MANUFACTURER CSV
def finding_fullinventory ():
    for j in manufacturersorted:
        for i in listsorteddate_wdetails:
            if (i [1] == j):
                FullInventory_List.append (i)
    # print ('Fullinventory',FullInventory_List)

#writing full inventory csv
def writing_csv_full_inventory ():
    with open ('FullInventory.csv', 'w') as Full_Inventory_csv_file:
        for i in FullInventory_List:
            Full_Inventory_csv_file.write (','.join(i))
            Full_Inventory_csv_file.write ('\n')

# print ('from writing past service date ', FullInventory_List)




#OUTSIDE of WITH OPEN
#FOR SEEING FULL INVENTORY LIST
# for i in FullInventory_List:
#     print(','.join(i))

# print (FullInventory_List)



#########################################


#PART B
#Finding different item types and adding into new list, sorted by types
def finding_diff_inv_types ():

    fullinventory_list =  FullInventory_List.copy()
    fullinventory_list.sort()
    for i in fullinventory_list:
        type = i [2]
        for i in fullinventory_list:
            if  i [2] == type:
                if i not in diff_inv_types:
                    diff_inv_types.append (i)
            else:
                continue

    # for i in diff_inv_types:
    #     print(','.join(i))


def writing_diff_inv_types ():
    typelist = []
    for i in range (len (diff_inv_types)-1):

        if diff_inv_types [i][2] == diff_inv_types [i+1][2] or (diff_inv_types [i][2] != diff_inv_types [i+1][2]):
            typelist.append (diff_inv_types[i])
        if (i == len (diff_inv_types) - 2 and diff_inv_types [i][2] == diff_inv_types [i+1][2]):
            typelist.append (diff_inv_types [i+1])


        elif (i == len(diff_inv_types) - 2) and (diff_inv_types[i][2] != diff_inv_types[i+1][2]):
            typelist.append (diff_inv_types[i+1])
            name = diff_inv_types[i+1][2]
            csvname = name.capitalize()
            with open(f'{csvname}Inventory.csv', 'w') as type_csv_file:
                diff_inv_types_COPY = typelist[len(typelist) - 1][:2] + typelist[len(typelist) - 1][3:]
                type_csv_file.write(','.join(diff_inv_types_COPY))
                type_csv_file.write('\n')
            typelist.pop (len(typelist)-1)


        if (diff_inv_types [i][2] != diff_inv_types [i+1][2]) or (i == len (diff_inv_types)-2):
            name = diff_inv_types [i][2]
            csvname = name.capitalize()

            with open(f'{csvname}Inventory.csv', 'w') as type_csv_file:
                for i in typelist:
                    diff_inv_types_COPY = i[:2]+i[3:]
                    type_csv_file.write(','.join(diff_inv_types_COPY))
                    type_csv_file.write('\n')

            typelist.clear()


##################################

#PART C
def finding_pastservicedates():
    currentdate = datetime.today()

    for i in FullInventory_List:
        dateobject1 = datetime.strptime(i[4],"%m/%d/%Y")

        if dateobject1 < currentdate:
            PastServiceDate_List.append (i)
    # print ('Past service date list',PastServiceDate_List)

def writing_csv_past_service_date_inventory ():

    with open ('PastServiceDateInventory.csv', 'w') as Past_Service_Date_Inventory_csv_file:
        for q in PastServiceDate_List:
            PastServiceDate_ListCOPY = q [:5]
            Past_Service_Date_Inventory_csv_file.write (','.join (PastServiceDate_ListCOPY))
            Past_Service_Date_Inventory_csv_file.write('\n')






#PART D
def finding_damaged_inventory ():
    #sorting full inventory from greatest to least price
    for j in pricesorted_wdetails:
        for i in FullInventory_List:
            if i[3] == j[1]:
                mostexpensive_to_least_list.append (i)
    # print ('price least to greatest',mostexpensive_to_least_list)

    #Finding damaged inventory
    for l in mostexpensive_to_least_list:
        if l [5] == 'damaged':
            damaged_inventory_list.append (l)
    # print ('damaged inventory listt',damaged_inventory_list)

def writing_csv_dmg_inventory ():
    with open ('DamagedInventory.csv', 'w') as damaged_inventory_csv_file:
        for q in damaged_inventory_list:
            damaged_inventory_listCOPY = q [:5]
            damaged_inventory_csv_file.write (','.join (damaged_inventory_listCOPY))
        damaged_inventory_csv_file.write ('\n')





if __name__ == '__main__':
#PART A
#Outputting full inventory
    finding_fullinventory()
    # print ('full inventory list after finding full inventory method is called',FullInventory_List)
    writing_csv_full_inventory()

#PART B
#Outputting Item type Inventory list
    finding_diff_inv_types()
    writing_diff_inv_types()

#PART C
#Outputting past service dates inventory
    finding_pastservicedates()
    # print ('past service date list after findingPastServicedates called',PastServiceDate_List)
    # print ('full inventory after findingpastservice dates called',FullInventory_List)

    writing_csv_past_service_date_inventory()
    # print ('full inventory after writingpastservice dates called',FullInventory_List)



#PART D
    #Outputting damaged inventory
    finding_damaged_inventory()
    writing_csv_dmg_inventory()
    # print ('dmg inventory last', damaged_inventory_list)












