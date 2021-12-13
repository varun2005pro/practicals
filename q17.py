a=float(input("Enter height in cm= "))
a=a/100
b=float(input("Enter weight in kg= "))
c= b/a**2
if (c<18.5):
    print("Underweight ")
elif (c>=18.5 or c<=24.9):
    print("Normal ")
elif (c>=25 or c<=29.9):
    print("overweight")
elif (c>30):
    print("Obesed")

#BY VARUN GAUTAM XI-A 
