#Default function to implement conditions to check leap year
def CheckLeap(Year):
    #checking if the given year is leap year 
    if((Year%400==0)or
      (Year%100!=0)and
      (Year%4==0)):
      print("Given year is a leap year")
      #Else it is not leap year
    else:
          print("Given year is not leap year")
        #taking an input year from user
Year=int(input("Enter the year. : "))
        #printing result
CheckLeap(Year)
