for x in range(1,10):
    if(x==5):
        break
    else:
        print('x=',x)
print('break out of loop at x=',x)
print('End!')

print('\n')

#最多接收50个整数，并计算他们的累加和。如果输入过程中输入了0，则循环立即停止输入，输出累加时的结果。
sum=0   #设置变量初始值
for i in range(1,51):
    num=input('Please enter a number:')
    num=int(num)    #将输入的字符串数字转化为十进制数字
    if(num==0):
        break   #输入的是0，则强制退出循环
    else:
        sum+=num    #输入的不是0，则进行累加后继续循环
print('The sum is=',sum)

