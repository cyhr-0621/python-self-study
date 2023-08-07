yz1=('zhang da hua',78,'male')
yz2=('li wei',59,'male')
yz3=('chen chun ting',76,'female')
yz4=('ni nai hui',45,'female')
yz5=('jing tao hai',49,'male')
zyz=(yz1,yz2,yz3,yz4,yz5)   #此元组里的每一个元素，又都是一个元组
for i in range(0,5):
    for item in (zyz[i]):
        print('%15s'%item,end='')   #函数print（）的格式化输出，保证数据右对齐
    print('\n')
print('End!')


