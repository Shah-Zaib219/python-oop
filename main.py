# ##################          #Level ONE
# print('Hello Python')
# name=input('Enter your name: ')
# print(f'Welcome {name}')
# age=21
# city='Abbottabad'
# print(f'Welcome {name}, from {city}, age is {age}')
# print(type(10), type(10.5), type('zaib'), type(True))
# a=10
# b=20
# a,b=b,a
# print(a,b)
# num1=int(input('Enter 1st number:'))
# num2=int(input('Enter 2nd number: '))
# print(f'Sum is {num1+num2}')
# print(f'Differnece is {num1-num2}')
# print(f'Multiplication {num1*num2}')
# print(f'Division {num1/num2}')


# num3=int(input('Enter a number:'))
# if num3%2==0:
#     print('Even')
# else:
#     print('odd')

# num4=int(input('Enter a number:'))
# num5=int(input('Enter another number:'))
# if num4>num5:
#     print(f'{num4} is greater than {num5}')
# elif num5>num4:
#     print(f'{num5} is greater than {num4}')

# num6=int(input("Enter value"))
# print(2*3.14*(num6**2))

####################      Level TWO

#############      String Operations
s1="Python"
s2="Programming"
s3=s1+" "+s2
print(s3)
s4="Hi!"
print((s4+" ")*5)
s5="Hello World"
print(len(s5))
print(s1[0])
print(s1[-1])
print(s1[2])

s6="PythonProgramming"
print(s6[0:6])
print(s6[6:len(s6)])
print(s6[2:10])

s7='PyThOn'
print(s7.upper())
print(s7.lower())
print(s7.title())

s7="banana"
print(s7.count('a'))

s8="I like Coffee"
print(s8.replace('Coffee','Tea'))

s9="   Python   "
print(s9.strip())
s9=s9.strip()
print(s9)

print(s9[::-1])  #was incorrctly written as print(s9.reverse()) which is not a valid method for strings. The correct way to reverse a string in Python is to use slicing with a step of -1, as shown above.
