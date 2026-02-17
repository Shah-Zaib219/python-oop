

# Level 1 - Basics

# Print greeting and user name
print('Hello Python')
name = input('Enter your name: ')
print(f'Welcome {name}')

# Variables
age = 21
city = 'Abbottabad'
print(f'Welcome {name}, from {city}, age is {age}')

# Data types
print(type(10), type(10.5), type('zaib'), type(True))

# Swap values
a, b = 10, 20
a, b = b, a
print(f'Swapped values: a={a}, b={b}')

# Arithmetic operations
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
print(f'Sum: {num1 + num2}')
print(f'Difference: {num1 - num2}')
print(f'Multiplication: {num1 * num2}')
print(f'Division: {num1 / num2}')

# Even or Odd
num3 = int(input('Enter a number: '))
if num3 % 2 == 0:
    print('Even')
else:
    print('Odd')

# Compare numbers
num4 = int(input('Enter a number: '))
num5 = int(input('Enter another number: '))
if num4 > num5:
    print(f'{num4} is greater than {num5}')
elif num5 > num4:
    print(f'{num5} is greater than {num4}')
else:
    print('Both numbers are equal')

# Circle area approximation (using pi ≈ 3.14)
radius = int(input('Enter radius of circle: '))
area = 2 * 3.14 * (radius ** 2)
print(f'Area of circle: {area}')
