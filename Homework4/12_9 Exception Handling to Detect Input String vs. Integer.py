#Kaitlyn Sourignosack
#1824497

parts = input().split()
name = parts[0]

while name != '-1':

    try:
        age = int(parts[1])
        age = int(parts[1]) + 1
        print(f'{name} {age}')


    except ValueError:
        parts [1] = 0
        age = parts [1]
        name = parts[0]
        print (f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]