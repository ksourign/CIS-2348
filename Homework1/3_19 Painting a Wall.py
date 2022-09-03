#Kaitlyn Sourignosack
#1824497

wallheight = int(input("Enter wall height (feet):""\n"))
wallwidth = int(input("Enter wall width (feet):""\n"))
wallarea = wallheight * wallwidth

print ("Wall area:", wallarea, "square feet")

paintneeded = wallarea / 350
print ("Paint needed:",'{:.2f}'.format(paintneeded), "gallons")

print ("Cans needed:", round (paintneeded), "can(s)""\n")

choosecolor = str (input("Choose a color to paint the wall:""\n"))



if(choosecolor == "red" or choosecolor == choosecolor =="RED" or choosecolor =="Red"):
    cost = 35
elif(choosecolor == "blue" or choosecolor == "BLUE" or choosecolor == "Blue"):
    cost = 25
elif(choosecolor == "green" or choosecolor == "GREEN" or choosecolor =="Green"):
    cost = 23
cost = cost*round(paintneeded)

print(f"Cost of purchasing {choosecolor} paint: ${cost}")

