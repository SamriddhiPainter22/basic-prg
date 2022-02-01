number=int(input("Enter a no. of which user wants to print themultiplication table : "))

#we are using 'for loop' to iterate the multiplication 10 times

print("The Multiplication table of : ")

for count in range(1,11):
    print(number,'x',count,'=',number*count)
    