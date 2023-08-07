#<列表名>[行索引][列索引]
#输入2行3列的列表的元素值，将其转置（即行列交换）后形成一个3行2列的列表
ls1=[[0,0,0],[0,0,0]]
ls2=[[0,0],[0,0],[0,0]]
print('Please enter 6 elements:')
for j in range(0,2):
    for k in range(0,3):
        ls1[j][k]=input()
for j in range(0,3):
    for k in range(0,2):
        ls2[j][k]=ls1[k][j]
print(ls1)
print(ls2)
print('End!')
