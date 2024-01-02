x=int(input('Enter 1st Value; '))
y=int(input('Enter 2nd Value; '))
a=x
b=y
print('Addtion: ',a+b)
print('Subtraction: ',a-b)
print('Multiplication: ',a*b)
print('Division: ',a/b)
print('Floor Division: ',a//b)
print('Modulus: ',a%b)
print('Power: ',a**b)
if a+b==b+a and a-b==b-a and a*b==b*a and a/b==b/a :
    print("it is Commutative Property")
else:
    print('it is not a Commutative Property')
