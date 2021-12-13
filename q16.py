num=int(input("Enter a no. = "))
sum=0
x=num
while x>0:
    digit = x%10
    sum=sum+digit**3
    x=x//10
if num == sum:
    print(num,"is an Armstrong")
else:
    print(num,"is not an Armstrong")

    #BY VARUN GAUTAM XI-A 