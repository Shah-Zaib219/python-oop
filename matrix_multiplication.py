
matrix1=[
    [1,2,3],[4,5,6],
    [7,8,9]
]
matrix2=[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
matrix3=[]
dummy_list=[]
for i in range(0,3):
    for j in range(0,3):
        dummy_list.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(dummy_list)
    dummy_list=[]
print(matrix3)    
