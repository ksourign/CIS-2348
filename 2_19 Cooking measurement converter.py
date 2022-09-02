#Kaitlyn Sourignosack
#1824497
lemonjuice = int(input("Enter amount of lemon juice (in cups):""\n"))
water = int(input("Enter amount of water (in cups):""\n"))
agavenectar = float(input("Enter amount of agave nectar (in cups):""\n"))
servings = float(input("How many servings does this make?""\n""\n"))


print("Lemonade ingredients - yields " '{:.2f}'.format(servings), "servings")
flemonjuice = float (lemonjuice)
fwater = float (water)
fagavenectar = float (agavenectar)

print('{:.2f}'.format(flemonjuice), "cup(s) lemon juice")
print('{:.2f}'.format(fwater), "cup(s) water")
print('{:.2f}'.format(fagavenectar), "cup(s) agave nectar""\n")


#how many servings would i like to make

servings2 = int(input("How many servings would you like to make?""\n""\n"))

print("Lemonade ingredients - yields " '{:.2f}'.format(servings2), "servings")

conversion = servings2/6
lemonjuice = lemonjuice * conversion
water = water * conversion
agavenectar = agavenectar * conversion


flemonjuice = float (lemonjuice)
fwater = float (water)
fagavenectar = float (agavenectar)

print('{:.2f}'.format(flemonjuice), "cup(s) lemon juice")
print('{:.2f}'.format(fwater), "cup(s) water")
print('{:.2f}'.format(fagavenectar), "cup(s) agave nectar""\n")

#gallons
print("Lemonade ingredients - yields " '{:.2f}'.format(servings2), "servings")
gallonlemon = flemonjuice / 16
gallonwater = fwater / 16
gallonagavenectar = fagavenectar/ 16

print('{:.2f}'.format(gallonlemon), "gallon(s) lemon juice")
print('{:.2f}'.format(gallonwater), "gallon(s) water")
print('{:.2f}'.format(gallonagavenectar), "gallon(s) agave nectar")
