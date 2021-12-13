a=eval(input("Please enter a list = "))
x,y=float('inf'),float('inf')
for i in a:
    if i<x:
        x,y=i,x
    elif i < y :
        y=i
print("lowest no. in a list = ",x)
print('Second lowest no. in a list = ',y)

#BY VARUN GAUTAM XI-A 
