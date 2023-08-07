#计算1~99的奇数之和
sum=0
for count in range(1,100,2):    #stop值必须设为100，否则就漏掉了99
    sum+=count
else:
    print('odd number cumulative sum',sum)
print('End!')

print('\n')

#求200以内，能被17整除的最大正整数
for x in range(17,200,17):
    if(x%17==0):    #满足整除
        if(x+17>=200):  #满足最大
            print(x)
print('End!')

#以上还可以使用break函数提前结束循环，使程序执行效率更高
for y in range(200,0,-1):   #倒序循环使其效率变高
    if(y%17==0):
        print(y)
        break
print('End!')



