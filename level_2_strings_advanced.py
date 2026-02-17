# Advanced String Operations

# 1. Uppercase parts and concatenate
s1 = 'PythonProgramming'
s11 = s1[0:6].upper()        # 'PYTHON'
s12 = s1[6:-1].upper()       # 'PROGRAMMIN' (last char excluded)
s2 = s11 + " - " + s12
print(s2)                    # Output: PYTHON - PROGRAMMIN

# 2. Reverse a string and repeat
s3 = 'Data'
print(s3[::-1] * 4)          # 'ataDataDataData'

# 3. Swap first 3 letters with last 3 letters
s4 = 'Programming'
first3 = s4[0:3]
last3 = s4[-3:]
s4_new = last3 + s4[3:-3] + first3
print(s4_new)                # Output: minggramPro

# 4. Count vowels in a string
s5 = "Abstraction"
print(f"a: {s5.count('a')}, e: {s5.count('e')}, i: {s5.count('i')}, o: {s5.count('o')}, u: {s5.count('u')}")

# 5. Splitting and recombining strings
s6 = "DataScience"
s61 = s6.split('Science')    # ['Data', '']
s62 = s6.split('Data')       # ['', 'Science']
print(s61, s62)

# Recombine in reverse order
s6_new = s62[1] + s61[0]
print(s6_new)                # 'ScienceData'

# 6. Access every 2nd character
s7 = "Programming"
print(s7[0:len(s7):2])       # 'Pormig'

# 7. Check if substring exists
s8 = "Hello Python"
print("Python" in s8)        # True

# 8. Replace all occurrences of a substring
s9 = "I like Python and Python is fun"
print(s9.replace('Python', 'Java'))  # 'I like Java and Java is fun'

# 9. Strip leading and trailing spaces
s10 = '    python programming    '
print(s10.strip())            # 'python programming'
