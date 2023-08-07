x1=input('Please enter first integer.')
x1=int(x1)
x2=input('Please enter second integer.')
x2=int(x2)
opt=input('Please enter an operator.')
if opt=='+':
    print('x1+x2=',x1+x2)
elif opt=='-':
    print('\nx1-x2=',x1-x2)
elif opt=='*':
    print('\nx1*x2=',x1*x2)
elif opt=='/':
    if(x2!=0):
        print('x1/x2=',x1/x2)
    else:
        print('\ndivision by zero!')
else:
    print('\nunkown operator!')
print('\nEnd!')

