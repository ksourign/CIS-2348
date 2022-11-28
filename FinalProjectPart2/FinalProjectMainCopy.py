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
sorted_pastservicedate = []

#lists for finding damaged inventory
oldest_to_recent_inventory = []
mostexpensive_to_least_list = []
damaged_inventory_list = []


#lists for Item type inventory list W DETAILS
diff_inv_types = []

#list for Item type ONLY
allitemtype = []

#list for III
suggestions = []


#list for PART II
positionlist = []




with open (r"ManufacturerList.csv", 'r') as csv_manufacturerfile:
    contentlist = csv.reader(csv_manufacturerfile)
    for i in contentlist:
        manufacturersorted.append(i[1])
        csvreader_copy.append (i)


# removing space in csv copy
    for i in range(len(csvreader_copy)):
        if csvreader_copy[i][1].find(' ') > -1:
            removespace = csvreader_copy[i][1][:len(csvreader_copy[i][1]) - 1]
            csvreader_copy[i][1] = removespace


# Remove extra space ahead of Manufacturer (Ex: Apple_ )
#manufac_set remove duplicates in manufacturer sorted
    for i in range(len(manufacturersorted)):
        if manufacturersorted[i].find(' ') > -1:
            removespace = manufacturersorted[i][:len(manufacturersorted[i]) - 1]
            manufacturersorted[i] = removespace
    manufac_set = set(manufacturersorted)


#SORTS A-Z in manufac_set IN manufacturersorted
    manufacturersorted = []
    for a in manufac_set:
        manufacturersorted.append (a)
    manufacturersorted.sort()


#manufacturesorted_wdetails include other details of the sorted manufacturers
    for i in range (len (manufacturersorted)) :
        for j in csvreader_copy:
            if (j[1] == manufacturersorted[i]):
                if j[1].find (' ') > -1:
                    j[1] = j[1][:j[1].find (' ')]
                    manufacturersorted[i] = manufacturersorted[i][:manufacturersorted[i].find (' ')]
                else:
                    manufacturersorted_wdetails.append (j)



#adding PRICE to correct id in manufacturer sorted w details
    for j in pricesorted_wdetails:
        for i in manufacturersorted_wdetails:
            if i[0] == j[0]:
                i.insert (3, j[1])



#adding DATES to correct id in manufacturersorted w details
    for j in listsorteddate_wdetails:
        for i in manufacturersorted_wdetails:
            if i[0] == j[0]:
                j.insert (1,i[1])
                j.insert (2,i[2])
                j.insert (3,i[3])
                j.insert (5,i[4])



#######################################


#PART A
#OUTSIDE OF GIVEN MANUFACTURER CSV
def finding_fullinventory ():
    for j in manufacturersorted:
        for i in listsorteddate_wdetails:
            if (i [1] == j):
                FullInventory_List.append (i)

#writing full inventory csv
def writing_csv_full_inventory ():
    with open ('FullInventory.csv', 'w') as Full_Inventory_csv_file:
        for i in range (len(FullInventory_List)):
            Full_Inventory_csv_file.write (','.join(FullInventory_List[i]))
            if i != len (FullInventory_List) - 1:
                Full_Inventory_csv_file.write ('\n')




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


#PART C
def finding_pastservicedates():
    #connecting sorted dates with ID details
    for i in range (len (listsorteddate_wdetails)):
        for j in range (len (FullInventory_List)):
            if listsorteddate_wdetails [i][0] == FullInventory_List [j][0]:
                oldest_to_recent_inventory.append (FullInventory_List[j])
            else:
                continue


    currentdate = datetime.today()

    for i in FullInventory_List:
        dateobject1 = datetime.strptime(i[4],"%m/%d/%Y")

        if dateobject1 < currentdate:
            PastServiceDate_List.append (i)


    for i in oldest_to_recent_inventory:
        if i in PastServiceDate_List:
            sorted_pastservicedate.append (i)



            
def writing_csv_past_service_date_inventory ():
    with open ('PastServiceDateInventory.csv', 'w') as Past_Service_Date_Inventory_csv_file:
        for q in sorted_pastservicedate:
            sorted_pastservicedate_ListCOPY = q [:5]
            Past_Service_Date_Inventory_csv_file.write (','.join (sorted_pastservicedate_ListCOPY))
            Past_Service_Date_Inventory_csv_file.write('\n')






#PART D
def finding_damaged_inventory ():
    #sorting full inventory from greatest to least price
    for j in pricesorted_wdetails:
        for i in FullInventory_List:
            if i[0] == j[0]:
                mostexpensive_to_least_list.append (i)

    #Finding damaged inventory
    for l in mostexpensive_to_least_list:
        if l [5] == 'damaged':
            damaged_inventory_list.append (l)

            
def writing_csv_dmg_inventory ():
    with open ('DamagedInventory.csv', 'w') as damaged_inventory_csv_file:
        for q in damaged_inventory_list:
            damaged_inventory_listCOPY = q [:5]
            damaged_inventory_csv_file.write (','.join (damaged_inventory_listCOPY))
            damaged_inventory_csv_file.write ('\n')







##### PART 2 #####
def printmenu():
    print('Enter \"q\" to Quit')


#Finding all different inventory types and putting into list
def finding_allitemtype():
    for i in diff_inv_types:
        allitemtype.append (i[2])



def ifdamaged (itemdetail):
    if itemdetail[5] == 'damaged':
        return True
    else:
        return False

def ifpastservicedate (itemdetail):
    if itemdetail in PastServiceDate_List:
        return True
    else:
        return False

def countoccurences (manufacturer, itemtype):
    count = 0
    for i in range (len (FullInventory_List)):
        if (FullInventory_List[i][1].find(manufacturer) > -1) and (FullInventory_List[i][2].find(itemtype) > -1):
            count += 2
    return int (count/2)



def findoccurence (manufacturer, itemtype):
    position = -1
    for i in range (len(FullInventory_List)):
        if (FullInventory_List[i][1].find(manufacturer) > -1) and (FullInventory_List[i][2].find(itemtype) > -1):
            position = i
    return position

def findoccurences (manufacturer, itemtype):
    for i in range(len(FullInventory_List)):
        if (FullInventory_List[i][1].find(manufacturer) > -1) and (FullInventory_List[i][2].find(itemtype) > -1):
            positionlist.append (i)
    return positionlist



def findmostexpensive (listofoccurences):
    mostexpensive = 0
    for i in listofoccurences:
        priceint = int(FullInventory_List[i][3])
        if priceint > mostexpensive:
            mostexpensive = priceint
            mostexpensive_item_pos = i
    return mostexpensive_item_pos



#III
def find_same_itemtype_suggestion (itemtype,pos):
    global suggestions
    suggestions = []
    for i in range (len (FullInventory_List)):
        if FullInventory_List[i][2] == itemtype and i != pos  and ifdamaged(FullInventory_List[i]) == False and ifpastservicedate(FullInventory_List[i]) == False and FullInventory_List[pos][1] != FullInventory_List[i][1]:
                suggestions.append (i)
    if len (suggestions) > 0:
        suggestion_pos = findmostexpensive(suggestions)
        printsuggestion(suggestion_pos)
    print ()



#Part III
def printsuggestion (pos):
    suggestionoutput = 'You may,also,consider: '
    itemoutput = FullInventory_List[pos][:4]

    for i in range (len (itemoutput)):
        if itemoutput[i].find(' ') > -1:
            word = itemoutput[i]
            itemoutput[i] = word[:word.find(' ')]
            suggestionoutput += itemoutput[i] + ','
        else:
            if i != len (itemoutput)-1:
                suggestionoutput += itemoutput[i] + ','
            else:
                suggestionoutput += itemoutput [i]
    print (suggestionoutput)

#Part II
def printitem (pos):
    output = 'Your item type is: '
    itemoutput = FullInventory_List[pos][:4]

    for i in range (len (itemoutput)):
        if itemoutput[i].find(' ') > -1:
            word = itemoutput[i]
            itemoutput[i] = word[:word.find(' ')]
            output += itemoutput[i] + ','
        else:
            if i != len (itemoutput)-1:
                output += itemoutput[i] + ','
            else:
                output += itemoutput [i]
    print (output)


 
#Finding a user's valid given manufacturer and itemtype in FullInventory list 
#OUTPUTTING DETAILS of the most expensive, non-damaged, not past service date item
def infullinventory (list):

    manufacturer_input = list [0].capitalize()
    itemtype_input = list [1].lower()

    new_occurencepositions = []

    if countoccurences (manufacturer_input.capitalize(), itemtype_input.lower()) == 1:

        position = findoccurence(manufacturer_input.capitalize(), itemtype_input.lower())
        if ifdamaged(FullInventory_List[position]) == False and ifpastservicedate(FullInventory_List[position]) == False:
            printitem(position)
            find_same_itemtype_suggestion(itemtype_input,position)
        else:
            print ('No such item in inventory')
            print ()

    elif countoccurences(manufacturer_input.capitalize(),itemtype_input.lower()) > 1:
        occurencepositions = findoccurences(manufacturer_input.capitalize(), itemtype_input.lower())
        for i in occurencepositions:
            if ifdamaged (FullInventory_List [i]) == False and ifpastservicedate(FullInventory_List[i]) == False:
                new_occurencepositions.append (i)

        if len (new_occurencepositions) > 0:
            position = findmostexpensive(new_occurencepositions)
            printitem(position)
            find_same_itemtype_suggestion(itemtype_input,position)
            new_occurencepositions.clear()
            occurencepositions.clear()


    else:
        print ('No such item in inventory')
        print ()



def inmanufacturersorted (manufacturer):
    manufacturer = manufacturer.capitalize()
    for i in range (len (manufacturersorted)):
        if manufacturersorted[i] == manufacturer:
            return i
        else:
            continue
    else:
        return False

#Checks if a word is in allitemtype list (all the differenty types in list)
def inallitemtype (word):
    word = word.lower()
    for i in range (len (allitemtype)):
        if allitemtype[i] == word:
            return i
        else:
            continue
    else:
        return False


def fixinputlist (irrelevantword):
    newlist = []
    firstmanufac = ''
    firsttype = ''
    #converts irrelevant word to lower so comparison works for lowercase only - avoiding ApPlE
    irrelevantword = irrelevantword.lower()

    countman = 0

    for i in manufacturersorted:

        if irrelevantword.find(i.lower())  > -1 and countman == 0:
            indexinstring =  irrelevantword.find(i.lower())

            for j in manufacturersorted:
                if irrelevantword.find(j.lower()) > -1:
                    index2 = irrelevantword.find(j.lower())
                    if index2 < indexinstring:
                        index2 = irrelevantword.find(j.lower())
                        newlist.append(j)
                        countman += 1
                        break
            else:
                newlist.append (i)
                break
        else:
            continue

            
            
    counttype = 0

    for i in allitemtype:
        if irrelevantword.find(i.lower())  > -1 and counttype == 0:
            indexinstring =  irrelevantword.find(i.lower())

            for j in allitemtype:
                if irrelevantword.find(j.lower()) > -1:
                    index2 = irrelevantword.find(j.lower())
                    if index2 < indexinstring:
                        index2 = irrelevantword.find(j.lower())
                        newlist.append(j)
                        counttype += 1
                        break
            else:
                newlist.append (i)
                break
        else:
            continue


    return newlist



if __name__ == '__main__':
#PART A
#Outputting full inventory
    finding_fullinventory()
    writing_csv_full_inventory()

#PART B
#Outputting Item type Inventory list
    finding_diff_inv_types()
    writing_diff_inv_types()

#PART C
#Outputting past service dates inventory
    finding_pastservicedates()
    writing_csv_past_service_date_inventory()


#PART D
#Outputting damaged inventory
    finding_damaged_inventory()
    writing_csv_dmg_inventory()


#############################################################################################

#Final Project PART 2
#putting all different item types in a list
    finding_allitemtype()

#Interactive INVENTORY QUERY capability
    printmenu()
    userinput = str(input('Enter manufacturer and item type: '))
    print ()

    while userinput != 'q' and userinput != 'Q':
        if userinput != 'q' and userinput != 'Q':
            inputlist = fixinputlist (userinput)
            if len (inputlist) == 2:
                infullinventory(inputlist)
                inputlist.clear()
            else:
                print ('No such item in inventory')
                print ()

        elif userinput == 'q' and userinput != 'Q':
            break


        printmenu()
        userinput = str(input('Enter manufacturer and item type: '))
        print ()


