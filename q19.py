sen = input("enter a sentance = ")
count = 1
alp = 0
for i in sen :
    if i == " " :
        count += 1
    elif i.isalnum() :
        alp += 1
print("number of word is ", count)
print("number of characters ", len(sen))
print("percentage of alpha numeric = ", (alp / len(sen)) * 100)

#BY VARUN GAUTAM XI-A 