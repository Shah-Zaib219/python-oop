##################          #Level ONE
print('Hello Python')
name=input('Enter your name: ')
print(f'Welcome {name}')
age=21
city='Abbottabad'
print(f'Welcome {name}, from {city}, age is {age}')
print(type(10), type(10.5), type('zaib'), type(True))
a=10
b=20
a,b=b,a
print(a,b)
num1=int(input('Enter 1st number:'))
num2=int(input('Enter 2nd number: '))
print(f'Sum is {num1+num2}')
print(f'Differnece is {num1-num2}')
print(f'Multiplication {num1*num2}')
print(f'Division {num1/num2}')


num3=int(input('Enter a number:'))
if num3%2==0:
    print('Even')
else:
    print('odd')

num4=int(input('Enter a number:'))
num5=int(input('Enter another number:'))
if num4>num5:
    print(f'{num4} is greater than {num5}')
elif num5>num4:
    print(f'{num5} is greater than {num4}')

num6=int(input("Enter value"))
print(2*3.14*(num6**2))


