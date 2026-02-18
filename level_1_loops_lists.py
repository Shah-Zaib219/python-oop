# Level 1 — Basic Logic, Loops, and Lists

# 1. Print numbers from 1 to 100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=' ')
print("\n")  # Add newline for readability

# 2. Print even numbers from 1 to 50
print("Even numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print("\n")

# 3. Sum of numbers from 1 to a given number
num = int(input('Enter a number to sum from 1 to n: '))
total = 0
for i in range(1, num + 1):
    total += i
print(f"Sum of numbers from 1 to {num} is {total}")

# 4. Multiplication table for a given number
num1 = int(input('Enter a number to see its multiplication table: '))
print(f"Multiplication table for {num1}:")
for i in range(1, num1 + 1):
    print(f"{i} x {num1} = {i * num1}")

# 5. Count number of digits in a number
num2 = int(input("Enter a number to count its digits: "))
count = 0
temp = num2
while temp != 0:
    temp //= 10
    count += 1
print(f"Number of digits in {num2} is {count}")
