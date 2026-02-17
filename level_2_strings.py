# Level 2 - String Operations

# Concatenation and repetition
s1 = "Python"
s2 = "Programming"
s3 = s1 + " " + s2
print(s3)

s4 = "Hi!"
print((s4 + " ") * 5)

# Length and indexing
s5 = "Hello World"
print(len(s5))
print(s1[0], s1[-1], s1[2])

# Slicing
s6 = "PythonProgramming"
print(s6[0:6])       # Python
print(s6[6:len(s6)]) # Programming
print(s6[2:10])      # thonProg

# String case methods
s7 = 'PyThOn'
print(s7.upper())
print(s7.lower())
print(s7.title())

# Count and replace
s7 = "banana"
print(s7.count('a'))

s8 = "I like Coffee"
print(s8.replace('Coffee', 'Tea'))

# Strip whitespace
s9 = "   Python   "
print(s9.strip())

s9 = s9.strip()
print(s9)

# Reverse string
print(s9[::-1])
