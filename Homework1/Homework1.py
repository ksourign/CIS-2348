#Kaitlyn Sourignosack
#1824497


Cmonth = int (input("Please enter current month: "))
Cday = int (input("Please enter current day: "))
Cyear = int (input("Please enter current year: "))


Bmonth = int (input("Please enter birth month: "))
Bday = int (input("Please enter birth day: "))
Byear = int (input("Please enter birth year: "))

print ("Birthday Calculator")

print("Current day")
print("Month:", Cmonth)
print("Day:", Cday)
print("Year:", Cyear)
print ("Birthday")
print ("Month:", Bmonth)
print ("Day:", Bday)
print ("Year:", Byear)

age = int()

if ((Cmonth == Bmonth) & (Cday == Bday)):
    print("Happy Birthday!")

elif ((Cmonth == Bmonth) & (Cday > Bday)):
    age = Cyear - Byear
    print("You are ", age, "years old.")

elif ((Cmonth == Bmonth) & (Cday < Bday)):
    ageNotChanged = (Cyear - Byear)-1
    print("You are ", ageNotChanged, "years old.")

elif ((Cmonth < Bmonth)):
    ageNotChanged = (Cyear - Byear) - 1
    print ("You are ", ageNotChanged, "years old.")

elif ((Cmonth > Bmonth)):
    age = Cyear - Byear
    print ("You are ", age, "years old.")


