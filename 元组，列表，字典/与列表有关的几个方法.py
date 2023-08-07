#append() 将给出的元素作为参数，添加调用该方法的列表的末尾
#<列表名>.append(<元素>)
staf=[('Ni_lin','male'),40,['1978:bron','2002:graduation','2002:enlist']]
print(type(staf[2]))
staf[2].append('2012:teacher')
print('\n',staf)
print('\n',staf[2])
print('\n',staf[2][3])
print('End!')

print('\n')

#insert() 将元素按照指定的索引位置，插入调用此方法的列表
#<列表名>.insert(i,<元素>)
staf=[('Ni_lin','male'),40,['1978:bron','2002:graduation','2002:enlist']]
staf[2].insert(1,'1996:worker') #在原元素位置插入，原元素及后面元素向后移
print('\n',staf[2])
print('\n',staf[2][1])
print('End!')

print('\n')

#extend() 将另一个列表中的所有元素添加到列表的末尾
#<列表名>.extend(<新列表名>)
month=['1','2','3','4','5','6'] #原列表
others=['7','8','9','10','11','12'] #新列表
month.extend(others)    #调用方法extend
i=1 #控制一行输出7个列表元素
for x in month:
    print(x+'',end='')
    i+=1
    if i==8:
        i=1
        print('\n')
    else:
        continue
print('End!')

print('\n')

#remove() 将指定元素从列表中删除
#<列表名>,(<元素>)
x=[3,5,3,5,3,5,3,5,3]
for i in x:
    if i==3:
        x.remove(i)
print(x)
y=[3,5,3,5,3,5,3,3,3]
for j in y:
    if j==3:
        y.remove(j)
print(y)

print('\n')

#pop() 按特定的索引值，删除列表中的某个元素；如果省略索引值，则表示删除列表末尾的最后一个元素；调用该方法后，会返回删除的元素。
#<列表名>.pop.(<索引值>)
staf=[('Ni_lin','male'),40,['1978:bron','2002:graduation','2002:enlist']]
x=staf[2].pop(1)    #可将删除的内容，保存到变量x里
print('\n',staf[2])
print('\n',x)
print('End!')

print('\n')

#clear() 清除列表中的所有元素
#<列表名>.clear()

#sort() 对列表元素进行排序
#<列表名>.sort(reverse) -->顺序排列
#<列表名>.sort(reverse=True) -->降序排列

lst=['1','2','3','4','5']
print(lst)
lst.sort()  #对列表lst进行升序排列
print(lst)
lst2=['1','2','3','4','5']
print(lst2)
lst2.sort(reverse=True)
print(lst2)
print('End!')

print('\n')

#sorted() 对元组或列表进行排序，返回排序后的新列表，原元组或列表保持不变
#sorted(<元组名/列表名>，reverse) -->升序
#sorted(<元组名/列表名>，reverse=True) -->降序

#reverse() 对列表元组进行原地旋转
#<列表名>.reverse()

#count() 返回指点元素在列表中出现的次数
#<列表名>.count(<元素名>)

#split() 将所给元素拆分成一个列表
#<变量名>.split(sep)   sep=''

