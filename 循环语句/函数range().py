#range(start,stop,step)  range(起始值，终止值，步长) 终止值不可省略
s='How are you?'
y=len(s)
for x in range(y):
    print(s[x])
else:
    print('End')

count=0
for y in range(126,997,10):
    if (y%3==0): #循环体
        print(y)
        count+=1
    else:
        print('count=',count)


