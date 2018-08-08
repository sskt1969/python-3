n = int(input("enter a number: "))
length = len(str(num))
sum = 0
temp = n
while(temp != 0):
    sum = sum + ((temp % 10) ** length)
    temp = temp // 10
if sum == n:
    print("it is armstrong number")
else:
    print("it is not a armstrong number")
