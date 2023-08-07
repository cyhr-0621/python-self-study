#iter() 从字典中不断取出“键-值”对中的键，与for循环连用时，就能够遍历字典中所有元素
code={'Li pin':356712,'Chen yun':125458,'Wen ti':894563,
      'Lin ling':337682,'Ru nin':675446,'Tang xi':345890}
for name in iter(code):
    print("%10s:%8d"%(name,code[name]))
else:
    print('End!')

print('\n') #修改一下程序

for i in iter(code):
    print('key: '+i)
    print('value: '+str(code[i]))
else:
    print('End!')

print('\n')

#item() 方法item()能够不断从字典中返回一个“键-值”对，借助for循环，可以直接获得“键”和“值”。
#<字典>.item()
for name,num in code.items():
    print('key: '+name)
    print('value: '+str(num))
else:
    print('End!')

print('\n')

#keys() 如果只是需要遍历和获取字典中的“键”，那么可以在程序中与for循环配合，使用方法keys()来实现
#<字典名>.keys()
for name in code.keys():
    print('key: '+name) #可以获取字典中诸多的“键”，而不涉及他们的“值”
else:
    print('End!')

print('\n')

#values() .......................“值”,...............................values()...
#<字典名>.values()
for value in code.values():
    print('value: '+str(value))
else:
    print('End!')

print('\n')

#sorted() 根据<字典名>后调用的是方法keys()或方法values()，方法sorted()将对该字典的元素，按键或按值进行默认的升序排列（参数reverse改为reverse=True则为降序排列）
#sorted(<字典名>.keys()/values(),reverse)
for name in sorted(code.keys()):
    print('key: '+name)
else:
    print('End!')
for num in sorted(code.values()):
    print('value: '+str(num))
else:
    print('End!')

print('\n')

#get() 字典调用方法get()时，返回键key所对的值。如果在字典中没有键名,则返回值None
#<字典名>.get(key,default)
print(code.get('Li pin'))
print(code.get('cyhr'))
if(code.get('cyhr'))==None:
    print('There is no key in dictionary:'+'cyhr')
print('End!')

print('\n')

#update() 合并两个字典，如果有相同的“键”，则添加字典的“值”作为该“键”最终对应的值
#<字典名1>.update(<字典名2>)
lit1={'name':'Ni hui-fen','age':32,'sex':'male'}
lit2={'Mathematics':84,'Geography':66,'Computer':95}
lit1.update(lit2)   #调用方法update()
for i in iter(lit1):
    print('key: '+i)
    print('value: '+str(lit1[i]))
print(lit2)
print('End!')

print('\n')

#popitem() 删除字典的最后一个元素，并返回他的“键-值”对
#<字典名>.popitem()
lit1.update(lit2)
for i in (lit1):
    print('key: '+i)
    print('value: '+str(lit1[i]))
x,y=lit1.popitem()
print('x=',x)
print('y=',y)
x,y=lit1.popitem()
print('x=',x)
print('y=',y)
print(lit1)
print(lit2)
print('End!')

