#<变量名>={<数据表>}
code={'Li pin':356712,'Chen yun':125458,'Wen ti':894563,
      'Lin ling':337682,'Ru nin':675446,'Tang xi':345890}
print(type(code),'\n')
print(code['Lin ling'],'\n')
print(code['Tang xi'])

#修改字典中的值:<字典名>[<键名>]=<新值>
code['Li pin']=123456
print(code['Li pin'])

#增加字典中的“键-值”对:<字典名>[<新键名>]=<相应的值>
code['Wang sen']=987654 #往字典code里添加新的“键-值”对
print('\n','Wang sen\'s number is:',code['Wang sen'])
print('\n',code)

#删除字典中的“键-值”对:del <字典名>[<键名>]
del code['Wang sen']
print('\n',code)
print('End!')



