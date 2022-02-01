num=int(input("Enter a No. : "))

if num < 0:
    print("Enter a Positive no. : ")
else:
    sum=0

    #use while loop to iterate un till zero

    while(num>0):
        sum+= num
        num-= 1
        print("The sum is",sum)