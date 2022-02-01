num=int(input("Enter the number : "))
factorial = 1
if num<0:
    print("The factorial does not exist for negative no's")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of" , num,"is",factorial)