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

# ###################      Level TWO

# #############      String Operations
# s1="Python"
# s2="Programming"
# s3=s1+" "+s2
# print(s3)
# s4="Hi!"
# print((s4+" ")*5)
# s5="Hello World"
# print(len(s5))
# print(s1[0])
# print(s1[-1])
# print(s1[2])

# s6="PythonProgramming"
# print(s6[0:6])
# print(s6[6:len(s6)])
# print(s6[2:10])

# s7='PyThOn'
# print(s7.upper())
# print(s7.lower())
# print(s7.title())

# s7="banana"
# print(s7.count('a'))

# s8="I like Coffee"
# print(s8.replace('Coffee','Tea'))

# s9="   Python   "
# print(s9.strip())
# s9=s9.strip()
# print(s9)

# print(s9[::-1])  #was incorrctly written as print(s9.reverse()) which is not a valid method for strings. The correct way to reverse a string in Python is to use slicing with a step of -1, as shown above.


s1='PythonProgramming'
s11=s1[0:6].upper()
s12=s1[6:-1].upper()
s2=s11+" - "+s12
print(s2)


s3='Data'
print(s3[::-1]*4)

s4='Programming'
s41=s4[0:3]
s4=s4.replace(s4[0:3],s4[len(s4)-3:len(s4)])
s4=s4.replace(s4[len(s4)-3:len(s4)],s41[0:3])

print(s4)

s5="Abstraction"

print(f"a: {s5.count('a')}, e: {s5.count('e')}, i: {s5.count('i')}, o: {s5.count('o')}, u: {s5.count('u')}")

s6="DataScience"
s61=s6.split('Science')
s62=s6.split('Data')
print(s61)
print(s62)
s6=s62[1]+s61[0]
print(s6)

s7="Programming"
print(s7[0:len(s7):2])

s8="Hello Python"
print("Python" in s8)


s9="I like Python and Python is fun"
print(s9.replace('Python','Java'))

s10='    python programming    '
print(s10.strip())