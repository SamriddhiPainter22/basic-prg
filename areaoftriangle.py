
#Three sides of triangle a,b,c
a=float(input('Enter first side : '))
b=float(input('Enter second side : '))
c=float(input('Enter Third Side : '))

#calculate the semi-perimeter

s=(a+b+c)/2

#calculate the area of triangle

area=(s*(s-a)*(s-b)*(s-c))**0.5

print('The area of the triangle is %0.2f'%area)

