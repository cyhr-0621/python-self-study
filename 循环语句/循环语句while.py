#输出1~50的所有能被3整除的正整数
num=1   #控制循环执行的变量初值
i=0
while(num<=50):
    if(num%3==0):
        i+=1
        print(i,num)
        num+=1
    else:
        num+=1
else:
    print('Number of postive integersis in total=',i)
    print('End!')

print('\n')

#反复从键盘输入一个最多5位的正整数，计算并输出组成该数的各位数字之和
x1=x2=x3=x4=x5=0
x=input('Please enter a five bit positive integer.')
x=int(x)
while(x!=0):
    x5=x%10;x=x//10
    x4=x%10;x=x//10
    x3=x%10;x=x//10
    x2=x%10;x=x//10
    x1=x%10
    print('x1+x2+x3+x4+x5=',x1+x2+x3+x4+x5)
    x=input('\nPlease enter a five bit positive integer.')
    x=int(x)
else:
    print('Bye-Bye!')


