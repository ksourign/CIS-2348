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

#removing multiple types
# input_splitlist = []

#stuff for PART II
# output = 'Your item is: '
positionlist = []


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
    print ('manufacturersorted',manufacturersorted)





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
    # print (diff_inv_types)

##################################

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
    # print ('Past service date list',PastServiceDate_List)




    for i in oldest_to_recent_inventory:
        if i in PastServiceDate_List:
            sorted_pastservicedate.append (i)
    # print ('SORTED PAST',sorted_pastservicedate)



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

    # print ('price least to greatest',mostexpensive_to_least_list)
    # for i in mostexpensive_to_least_list:
    #     print(','.join(i))





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



#############################################################################################





##### PART 2 #####
def printmenu():
    print('Enter \"q\" to Quit')


#Finding all different inventory types and putting into list
def finding_allitemtype():
    for i in diff_inv_types:
        allitemtype.append (i[2])
    print ('allitemtype list',allitemtype)






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

# def ifoccurence (inputlist):
#     manufacturer = inputlist[0]
#     itemtype = inputlist [1]
#     for i in range (len(inputlist)):
#         if FullInventory_List.find (manufacturer) > -1 and FullInventory_List.find (itemtype):
#             count+= 2
#     return int (count/2)

def findoccurence (manufacturer, itemtype):
    position = -1
    for i in range (len(FullInventory_List)):
        if (FullInventory_List[i][1].find(manufacturer) > -1) and (FullInventory_List[i][2].find(itemtype) > -1):
            position = i
            # positionlist.append (i)
    # print (positionlist)
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



# III
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

#II
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


#Output the correct list by deleting all irrelevant words (works w spaced out inputs only)
def checkandremove_otherwords (list):
    removed = []
    # count = 0

    for i in list:
        if inmanufacturersorted(i) == True or inallitemtype(i) == True:
            # count += 1
            removed.append (i)
        else:
            continue
    return removed

    # if count > 0:
    #     return removed
    # else:
    #     return False





#FIND the user's given manufacturer
# and itemtype in list - OUTPUTTING DETAILS of the item
def infullinventory (list):
    print ('goes thru')

    manufacturer_input = list [0].capitalize()
    itemtype_input = list [1].lower()

    print (manufacturer_input, itemtype_input)
    new_occurencepositions = []

    if countoccurences (manufacturer_input.capitalize(), itemtype_input.lower()) == 1:
        # print ('occurences:',countoccurences (manufacturer_input.capitalize(), itemtype_input.lower()))

        position = findoccurence(manufacturer_input.capitalize(), itemtype_input.lower())

        if ifdamaged(FullInventory_List[position]) == False and ifpastservicedate(FullInventory_List[position]) == False:
            printitem(position)
            find_same_itemtype_suggestion(itemtype_input,position)
        else:
            print ('No such item in inventory')
            print ()

    elif countoccurences(manufacturer_input.capitalize(),itemtype_input.lower()) > 1:
        occurencepositions = findoccurences(manufacturer_input.capitalize(), itemtype_input.lower())
        # print ('occurencepositions',occurencepositions)
        for i in occurencepositions:
            if ifdamaged (FullInventory_List [i]) == False and ifpastservicedate(FullInventory_List[i]) == False:
                new_occurencepositions.append (i)
        # print ('new occurence positions', new_occurencepositions)

        position = findmostexpensive(new_occurencepositions)
        # print ('position',position)
        printitem(position)
        find_same_itemtype_suggestion(itemtype_input,position)
        occurencepositions.clear()
        new_occurencepositions.clear()

    else:
        print ('No such item in inventory')
        print ()

#this method exists all bc of the space in 'Apple '
#MUST use string.find () >-1
#ONLY works if you already know the established manufacturer you are looking for - THIS defines the user's input of what is a manufacturer
def inmanufacturersorted (manufacturer):
    manufacturer = manufacturer.capitalize()
    for i in manufacturersorted:
        if i.find (manufacturer) > -1:
            return True
        else:
            continue
    else:
        return False



def countmanufacturer (somelist):
    count = 0
    for i in range(len(somelist)):
        if (inmanufacturersorted(somelist[i]) == True):
            count += 1
    return count


def countmultipleitemtype (list):
    count = 0
    for i in list:
        if inallitemtype(i.lower()) == True:
            count += 1
    return count



#Checks if a word is in allitemtype list (all the differenty types in list)
def inallitemtype (word):
    word = word.lower()
    for i in allitemtype:
        if i.find (word) > -1:
            return True
        else:
            continue
    return False




def newinputlist_from_irrelevantstring (irrelevantword):
    newlist = []
    #converts irrelevant word to lower so comparison works for lowercase only - avoid ApPlE
    irrelevantword = irrelevantword.lower()
    for i in manufacturersorted:
        if irrelevantword.find(i.lower())  > -1:
            newlist.append (i)
        else:
            continue
    for i in manufacturersorted:
        if irrelevantword.find(i.lower())  > -1:
            newlist.append (i)
        else:
            continue

    return newlist





def checking_and_removing_multiple_types_and_manuf (list):
    countmanufac = 0
    print ('same manufacturer count:', countmanufacturer(list),'same itemtype count:',countmultipleitemtype(list))
    # print (manufacturersorted)
    if len (list) > 2:
        # print (countmultipleitemtype(list))
        # print (countmanufacturer(list))
        # print ('count item type variable', countitemtype)

        for i in range (len (list)):
            # and
            #gets the LAST REPEATED MANUFACTURER INDEX
            if (inmanufacturersorted(list[i]) == True):
                countmanufac += 1
                index = i
        #         print ('countman',countmanufac)
        #         print ('last index of repeated manufac', index)

            #counting itemtype
            # and countmultipleitemtype(list) > 1:
            if countmanufacturer(list) == 0:
                itemtype_sliced = list [:i+1]
                return itemtype_sliced
                break
            if countmultipleitemtype(list) == 0:
                manufac_sliced = list [i-1:]
                return manufac_sliced
                break
            if countmanufacturer (list) == 1 and countmultipleitemtype(list) > 1:

                if inallitemtype(list[i].lower()) == True:
                    index = i+1
                    newlist = list [:index]
                    return newlist
                    break



            #if there are manufacturer repeats - slice list when manufacturer repeats are counted AND multiple itemtypes == 1
            elif (countmanufacturer (list) > 1 and inallitemtype (list[i].lower()) == True and countmultipleitemtype(list) == 1):
                #must make new list to not alter original list's length
                manufac_sliced = list [i-1:]
                print ('GO THRU 1')
                return manufac_sliced
                # print ('slice manufacfsgs',manufac_sliced )
                break




            #if there are manufacturer repeats - slice list when manufacturer repeats are counted AND multiple itemtypes > 1
            elif (countmanufacturer(list) > 1 and countmultipleitemtype(list) > 1):
                #must make new list to not alter original list's length
                if inallitemtype(list[i].lower()) == True:

                    newlist = list [index:i+1]
                    # print ('mafnedfsd', manufac_sliced)
                    # for i in range (len (manufac_sliced)):
                    #     if inallitemtype(manufac_sliced[i].lower) == True:
                    #         index = i+1
                    #         print ('index', index)
                    #         break
                    # newlist = manufac_sliced [:index]
                    print ('GO THRU 2')
                    return newlist
                    # print ('slice manufacfsgs',manufac_sliced )
                    break

    else:
        print ('NORMAL OUTPUT with 2 inputs with spaceeee', end='')
        return list



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
            input_splitlist = userinput.split()
            # print ('input splitlst',input_splitlist)
            removed_irrelevant_words = checkandremove_otherwords(input_splitlist)
            removed_multiples = checking_and_removing_multiple_types_and_manuf(removed_irrelevant_words)

            if len (removed_multiples) < 2:
                print ('Item unavailable because length is only 1 which is:',removed_multiples)
            else:
                correctinput_splitlist = removed_multiples
                print ('CORRECT input splitlist',removed_multiples)
                infullinventory(correctinput_splitlist)



        elif userinput == 'q' and userinput != 'Q':
            print ('QUITTED')
            break


        printmenu()
        userinput = str(input('Enter manufacturer and item type: '))
        print ()


