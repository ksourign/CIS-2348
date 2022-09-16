#Kaitlyn Sourignosack
#1824497

user_pass = str (input())
new_pass = ''

for a in user_pass:
       if a == 'i':
              new_pass += '!'
       elif a == 'a':
              new_pass += '@'
       elif a == 'm':
              new_pass += 'M'
       elif a == 'B':
              new_pass += '8'
       elif a == 'o':
              new_pass += '.'
       else:
              new_pass += a

print (new_pass + 'q*s')