#Kaitlyn Sourignosack
#1824497

word = str (input())

wordnospace =''
reversedword = ''

for q in reversed (range (len(word))):
    if word[q] != ' ':
        reversedword += word[q]
for w in range (0, len(word)):
    if word[w] != ' ':
        wordnospace += word[w]

if wordnospace == reversedword:
    print (word, 'is a palindrome')
else:
    print (word, 'is not a palindrome')


