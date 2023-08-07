message='please wait beyond the line.'
print(message.title()) #首字母大写
print(message) #原样输出
message.title()
message1=message.title()
print(message1)
print(message.upper()) #将字符串内所有字母都改为大写
print(message.lower()) #将字符串内所有字母都改为小写

#字符串切片 [start:end:step]=[切片起始位置索引:切片终止位置索引:切片索引增（减）步长]
#str[m] 索引值为m
#str[m:n] m ~ n-1,左闭右开
#str[m:] m开始到字符串结束
#str[:n] 0开始到n-1
#str[:] 整个字符串
#str[::-1] 反转后的字符串

print('\n')

strl='I\'m a student'
print(strl[6])
print(strl[1:9])
print(strl[9:])
print(strl[:])
print(strl[::-1])
print(strl[0:14:2])



