#列表是可修改的，列表的可修改性是列表与元组间的最本质的差别

staf=[('Ni_lin',male),40,['1978:bron','2002:graduation','2002:enlist']]
print(staf[1])
staf[1]=41  #将列表中元素元组40修改为41
print(staf[1])
print('End!')

#元组可以是列表的元素，列表又具有可嵌套性，所以列表相对于元组更加的灵活
