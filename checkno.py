#default function to run if else condition
def NumberChecking(a):
    #Checking if the no is positive
    if a>0:
        print("the Number given by you is Positive")
        #checking if the no id negative
    elif a<0:
        print("The number given by you is negative")
    #Else the no is zero
    else:
        print("Number given by you is zero")
    #taking no from user
a=float(input("Enter a number as input value : "))
    #Printing resulting
NumberChecking(a)
        