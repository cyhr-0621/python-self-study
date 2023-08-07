#len() 求元组中元素的个数，即元组的长度
#len(<元组变量名>)
yz=('cyhr',18,'male')
len(yz)
print(len(yz))  #元组中有三个元素

print('\n')

#count() 求元组中某元素出现的个数
#<元组变量名>.count(<元组中的元素名>)
yz1=('zhang da hua',78,'male',)
yz2=('li wei',59,'male')
yz3=('chen chun ting',76,'female')
yz4=('ni nai hui',45,'female')
yz5=('jing tao hai',49,'male')
zyz=yz1+yz2+yz3+yz4+yz5   #拼接成一个大元组zyz
print('male=',zyz.count('male'),'female=',zyz.count('female'),end='\n')
print('End!')

print('\n')

#index() 获得某元素在元组中第1次出现的位置
#<元组变量名>.index(<元素名>,i,j)
#i是查找的开始位置的索引
#j是查找结束位置的索引
#i和j两个参数都可以省略，省略时表明是从头查到尾
print(zyz.index('male'))
print(zyz.index('male',6))  #从索引值为6的地方开始查找元素male第一次出现位置的索引值
print('End!')

