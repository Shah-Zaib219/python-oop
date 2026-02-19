# Level 3 — Lists and Dictionaries Practice

# 25. Add a new key-value pair to a dictionary
student = {"name": "Ali", "age": 21}
student['city'] = "Abbottabad"
print("After adding city:", student)

# 26. Add marks to student dictionary
student['marks'] = 3.75
print("After adding marks:", student)

# 27. Remove a key from the dictionary
student.pop('city')
print("After removing city:", student)

# 28. Count frequency of numbers in a list
list28 = [1,2,1,3,4,5,4,3,6,7,5,3,1,2,4,2,5,6,4,2,5,6,3,5,2,4,6,7,4]
numbers_count = {}
for i in list28:
    if i not in numbers_count:
        numbers_count[i] = list28.count(i)
print("Frequency of numbers:", numbers_count)

# 29. Count frequency of characters in a string
str29 = "python is fun python"
frequency_count = {}
for s in str29:
    if s not in frequency_count:
        frequency_count[s] = str29.count(s)
print("Character frequency:", frequency_count)

# 30. Find the highest marks in a dictionary
student_marks = {
    "student1": 15,
    "student2": 25,
    "student3": 95,
    "student4": 85,
    "student5": 75
}
highest_marks = float('-inf')
for student in student_marks:
    if student_marks[student] > highest_marks:
        highest_marks = student_marks[student]
print("Highest marks:", highest_marks)

# 31. Print students with marks greater than 75
students = {"Ali": 80, "Sara": 90, "Ahmed": 70}
for student in students:
    if students[student] > 75:
        print(student, "scored more than 75")

# 32. Combine two lists into a dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
key_values = {}
for i in range(len(keys)):
    key_values[keys[i]] = values[i]
print("Combined dictionary:", key_values)

# 33. Separate even and odd numbers from a list
numbers_list = [1,2,3,4,5,6,7,8,9,8,7,66,9,0,1,2,66]
even_list = []
odd_list = []
for i in numbers_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_odd = {"even": even_list, "odd": odd_list}
print("Even and odd numbers:", even_odd)

# 34. Simple bank menu using dictionary and while loop
bank_options = {
    1: 'deposit',
    2: 'withdraw',
    3: 'show balance',
    0: 'exit'
}

flag = True
while flag:
    print("\nBank Options:", bank_options)
    option = int(input("Enter a number: "))
    if option in bank_options and option != 0:
        print("Selected:", bank_options[option])
    elif option == 0:
        print("Exit")
        flag = False
    else:
        print('Enter a valid number')
