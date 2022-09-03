#Kaitlyn Sourignosack
#1824497

print ("Davy's auto shop services""\n"
"Oil change -- $35""\n"
"Tire rotation -- $19""\n"
"Car wash -- $7""\n"
"Car wax -- $12""\n")

service = str()
total = 0
service = str (input("Select first service:""\n"))
service1 = service
noservice1 = 0

#for printing

if(service1 == "oil change" or service1 == "Oil change"):
    price1 = 35
if (service1 == "tire rotation" or service1 == "Tire rotation"):
    price1 = 19
if (service1 == "car wash" or service1 == "Car wash"):
    price1 = 7
if (service1 == "car wax" or service1 == "Car wax"):
    price1 = 12
if (service1 == "-"):
    price1 = 0
    noservice1 = 1

#for totaling
if(service == "oil change" or service == "Oil change"):
    cost = 35
    total = total + cost
if (service == "tire rotation" or service == "Tire rotation"):
    cost = 19
    total = total + cost
if (service == "car wash" or service == "Car wash"):
    cost = 7
    total = total + cost
if (service == "car wax" or service == "Car wax"):
    cost = 12
    total = total + cost
if (service == "-"):
    cost = 0
    total = total + cost

service = str (input("Select second service:""\n"))
service2 = service
noservice2 = 0

#for printing
if(service2 == "oil change" or service2 == "Oil change"):
    price2 = 35
if (service2 == "tire rotation" or service2 == "Tire rotation"):
    price2 = 19
if (service2 == "car wash" or service2 == "Car wash"):
    price2 = 7
if (service2 == "car wax" or service2 == "Car wax"):
    price2 = 12
if (service2 == "-"):
    price2 = 0
    noservice2 = 1

#for totaling
if(service == "oil change" or service == "Oil change"):
    cost = 35
    total = total + cost
if (service == "tire rotation" or service == "Tire rotation"):
    cost = 19
    total = total + cost
if (service == "car wash" or service == "Car wash"):
    cost = 7
    total = total + cost
if (service == "car wax" or service == "Car wax"):
    cost = 12
    total = total + cost
if (service == "-"):
    cost = 0
    total = total + cost


print("")
print ("Davy's auto shop invoice""\n")

if (noservice1 == 1):
    print ("Service 1: No service")
    print(f"Service 2: {service2}, ${price2}""\n")
if (noservice2 == 1):
    print(f"Service 1: {service1}, ${price1}")
    print ("Service 2: No service""\n")

elif(noservice1 ==0 and noservice2 ==0):
    print (f"Service 1: {service1}, ${price1}")
    print (f"Service 2: {service2}, ${price2}""\n")

print(f"Total: ${total}")