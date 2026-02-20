
#     ******
for i in range(1, 6):
    print("*", end="")


##### square pattern
for i in range(1, 10):
    for i in range(1,6):
        print("*", end="")
    print("")


###### left triangle
for i in range(1, 6):
    for j in range(0, i):
        print("*",end="")
    print("")


######### reverse triangle
for i in range(6, 1, -1):
    for j in range(0, i):
        print("*", end="")
    print("")


### Right side triangle (space handling)
num = 5

for i in range(1, num + 1):
    
    # print spaces
    for j in range(num - i):
        print(" ", end="")
    
    # print stars
    for k in range(i):
        print("*", end="")
    
    print()