#元组元素具有不可修改性    属于“不可变数据类型”
#元组元素还具有顺序性
yz=('cyhr',18,'male')
for item in (yz):
    print(item,end='')  #end=''保证在一行上输出元组各元素
print('End!')
