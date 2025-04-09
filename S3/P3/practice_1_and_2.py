# d = {"cars": [], "home": []}
# print("whats mans 'cars' ?")
# d["cars"] = input("enter mans: ")
# print("whats mans 'home' ?")
# d["home"] = input("enter mans: ")
# print(d)
# #---------------------------------------#
# char = input("enter your word: ")
# print(d[char])

#*************************************************************

d ={}
key = input("word: ")
meanings = input("meanings: ").split(",")
d[key] = meanings

key = input("word: ")
meanings = input("meanings: ").split(",")
d[key] = meanings

#--------------------------2-----------------------------
word = input("your word: ")
print("meanings", d.get(word))