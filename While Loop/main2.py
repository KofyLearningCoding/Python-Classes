num=int(input("enter number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(f"{num} is an armstrong Number")
else:
    print(f"{num} is not an armstrong Number")