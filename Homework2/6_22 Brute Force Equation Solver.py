#Kaitlyn Sourignosack
#1824497

def firstequation (a,b,c,x,y):
    if (((a*x) + (b*y)) == c):
        return True
    return False

def secequation (d,e,f,x,y):
    if ((d * x) + (e * y)) == f:
        return True
    return False



a = int (input())
b = int (input())
c = int (input())
d = int (input())
e = int (input())
f = int (input())

solutions = 0

for x in range(-10,11):
    for y in range(-10,11):
        if ( (firstequation (a,b,c,x,y) & secequation (d,e,f,x,y) ) == True):
            solx = x
            soly = y
            solutions += 1
            print (solx,soly)
            break

if solutions == 0:
    print ('No solution')






