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


# s1='PythonProgramming'
# s11=s1[0:6].upper()
# s12=s1[6:-1].upper()
# s2=s11+" - "+s12
# print(s2)


# s3='Data'
# print(s3[::-1]*4)

# s4='Programming'
# s41=s4[0:3]
# s4=s4.replace(s4[0:3],s4[len(s4)-3:len(s4)])
# s4=s4.replace(s4[len(s4)-3:len(s4)],s41[0:3])

# print(s4)

# s5="Abstraction"

# print(f"a: {s5.count('a')}, e: {s5.count('e')}, i: {s5.count('i')}, o: {s5.count('o')}, u: {s5.count('u')}")

# s6="DataScience"
# s61=s6.split('Science')
# s62=s6.split('Data')
# print(s61)
# print(s62)
# s6=s62[1]+s61[0]
# print(s6)

# s7="Programming"
# print(s7[0:len(s7):2])

# s8="Hello Python"
# print("Python" in s8)


# s9="I like Python and Python is fun"
# print(s9.replace('Python','Java'))

# s10='    python programming    '
# print(s10.strip())


# #########     LEVEL 1 — Basic Logic + Loops + Lists

# for i in range(1,101):
#     print(i)


# for i in range(1,51):
#     if i%2==0:
#         print(i)

# num=int(input('Enter a number: '))
# total=0;
# for i in range(1, num):
#     total+=i
# print(total)

# num1=int(input('Enter a number: '))
# for i in range(1, num1+1):
#     print(f"{i} x {num1} = {i*num1}")


# num2=int(input('Enter a number: '))
# count=0
# while True:
#     if num2<=9:
#         count+=1
#         break
#     else:
#         num2=num2//10
#         count+=1
# print(count)

#### 6
# list1=[4,5,7,8,6]
# sum1=0
# avg=0
# largest=list1[0]
# smallest=list1[0]
# for num in list1:
#     sum1+=num
#     if num>largest:
#         largest=num
#     if num<smallest:
#         smallest=num

# avg=sum1/len(list1)
# print(f"Sum: {sum1}, Average: {avg}, Largest: {largest}, Smallest: {smallest}")

##### 7 8
# list2=list()
# even_count=0
# odd_count=0
# for i in range(1, 11):
#     num3=int(input('Enter a number: '))
#     if num3%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
#     list2.append(num3)
# print(list2)
# print("Even Counts: ", even_count)
# print("Odd Count: ", odd_count)

# ### 9
# list3=[4,6,9,1,77,9,5,2,99,0,889,5,6,8]
# maximum=list3[0]
# for num in list3:
#     if num>maximum:
#         maximum=num
# print(maximum)



# ###### 10

# list4=list()
# for i in range(len(list3), 0, -1):
#     list4.append(list3[i-1])
# print(list4)

# ######## 11
# num4=int(input("Ener a number: "))
# half=num4//2
# print(half)
# for i in range(2, half):
#     if num4%i==0:
#         print("Not Prime")
#         break

# ############# 12

# list5 = [44,4,4,6,9,1,77,9,5,2,99,0,889,5,6,8]
# list6 = []

# for item in list5:
#     if item not in list6:
#         list6.append(item)

# print(list6)



#### 15

# list7 = [80, 65, 45, 76, 7, 3, 45, 6]

# largest = second_largest = float('-inf')  # initialize to very small number
# print(largest)
# for i in list7:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i

# print("Largest:", largest)
# print("Second Largest:", second_largest)


# #### 17
# list8=[2,5,3,4,7,8,9,0,87,6,77,5,2,33,1,21,2,3,5,7,5,4,5,4,443,3,24,67,5,78,4]

# even_list8=[]
# odd_list8=[]

# for i in list8:
#     if i%2==0:
#         even_list8.append(i)
#     else:
#         odd_list8.append(i)

# print(even_list8)
# print(odd_list8)


# ##### 19
# name = "shah zaib"

# print(f"{name.count('a')} {name.count('e')} {name.count('i')} {name.count('o')} {name.count('u')}")


# str1="DEesED"
# flag=True
# for i in range(0,len(str1)//2):
#     j=len(str1)-i-1
#     if str1[i]==str1[j]:
#         flag=True
#     else:
#         flag=False
#         break
# if flag:
#     print('Palindome')
# else:
#     print('Not Palindrome')



# ######################  22
# for i in range(1,5):
#     for j in range(0,i):
#         print("*", end="")
#     print('')



# ############     23
# for i in range(1,11):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i*j}")


# ##### 24
# student={
#     'name': 'Shah Zaib',
#     'age': 23,
#     'marks': 3.71
# }
# print(student)


# #######   25
# student['city']="Abbottabad"
# print(student)


# ######## 26
# student['marks']=3.75
# print(student)



# ###### 27
# student.pop('city')
# print(student)



######## 28

# list28=[1,2,1,3,4,5,4,3,6,7,5,3,1,2,4,2,5,6,4,2,5,6,3,5,2,4,6,7,4]
# numbers_count={}
# for i in list28:
#     if i not in numbers_count:
#         n=list28.count(i)
#         numbers_count[i]=n
# print(numbers_count)


######## 29
# str29="python is fun python"
# frequency_count={}
# for s in str29:
#     if s not in frequency_count:
#         n=str29.count(s)
#         frequency_count[s]=n
# print(frequency_count)


# ########## 30
# studen_marks={
#     "student1": 15,
#     "student2": 25,
#     "student3": 95,
#     "student4": 85,
#     "student5": 75

# }
# highest_marks=float('-inf')
# studen_keys=studen_marks.keys()
# for student in studen_keys:
#     if studen_marks[student]>highest_marks:
#         highest_marks=studen_marks[student]
#     else:
#         pass
# print(highest_marks)

# ############  31

# students={"Ali":80,"Sara":90,"Ahmed":70}
# students_keys=students.keys()
# for student in students_keys:
#     if students[student] >75:
#         print(student)


# ####### 32
# keys = ["a","b","c"]
# values = [1,2,3]
# key_values={}
# for i in range(0, len(keys)):
#     key_values[keys[i]]=values[i]
# print(key_values)

# ####### 33
# even_list=[]
# odd_list=[]
# numbers_list=[1,2,3,4,5,6,7,8,9,8,7,66,9,0,1,2,66]
# even_odd={}
# for i in numbers_list:
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# even_odd["even"]=even_list
# even_odd['odd']=odd_list
# print(even_odd)


# ########## 34
# bank_options={
#     1: 'deposit',
#     2: 'withdraw',
#     3: 'show balance',
#     0: 'exit'
# }
# flag=True
# while flag:
#     print(bank_options)
#     option=int(input("Enter a number: "))
#     if option>=1 and option<=3:
#         print(bank_options[option])
#     elif option==0:
#         print("Exit")
#         flag=False
#     else:
#         print('Enter a valid Number')

#### LEVEL 1 — Basic Functions & Simple Classes (Foundation)
##### 1
# def sum():
#     num1=int(input('Enter a number: '))
#     num2=int(input('Enter a number'))
#     return num1+num2

# print(sum())


# ###### 2
# def even_odd():
#     num1=int(input('Enter a number: '))
#     if(num1%2==0):
#         print("Even")
#     else:
#         print("odd")

# even_odd()

###  3
# def square():
#     num1=int(input("Enter a number: "))
#     return num1*num1
# print(square())
