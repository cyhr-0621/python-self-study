'''

c = 1
b = 2
a = 3
ddd = c + \
      b + \
      a
print("111\r222")
*********************************************************
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
**********************************************************
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))


#字符串格式化代码：
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
x = 71.63
print(f"公司:{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%.1f,经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,x))

#数据输入input函数
user_name = input("请输入用户名称：")
user_type = input("请输入用户类型：")
print("您好:%s，您是尊贵的%s用户，欢迎您的光临"%(user_name,user_type))
print(f"您好:{user_name}，您是尊贵的{user_type}用户，欢迎您的光临")


print("欢迎来到黑马游乐园。")
body_height = int(input("请输入你的身高（cm）："))
if body_height > 120 :
    print("您的身高超出120cm，游玩需要购票10元。")
else :
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游戏愉快。")


'''
# if int(input("请输入第一次猜想的数字：")) == 10:
#     print("猜对了")
# elif int(input("不对，再猜一次：")) == 10:
#     print("猜对了")
# elif int(input("不对，再猜最后一次：")) != 10:
#     print("Sorry,全部猜错啦，我想的是10")

# import random
# num = random.randint(1,10)
# print("猜数字1-10")
#
# one = int(input("请输入一个数："))
#
# if one == num:
#     print("猜对了")
# else:
#     if one < num:
#         print("小了")
#     if one > num:
#         print("大了")
#
#     two = int(input("再试一次："))
#     if two == num:
#         print("猜对了")
#     else:
#         if two > num:
#             print("大了")
#         if two < num:
#             print("小了")
#
#         three = int(input("最后一次："))
#         if three == num:
#             print("猜对了")
#         else:
#             if three < num:
#                 print("小了")
#             if three > num:
#                 print("大了")


# i = 1
# z = 0
# while i <= 100:
#     z = z + i
#     i += 1
# print(z)


# import random
# num = random.randint(1,10)
# i=1
# a=int(input("请输入一个数："))
# while a != num:
#     a=int(input("再试一次："))
#     i += 1
# print("猜对了")
# print("一共猜了%d次"%(a))

# import random
# num = random.randint(1,10)
# flag = True
# i = 0
# while flag:
#     gess_num = int(input("请输入一个数字："))
#     i += 1
#     if gess_num == num:
#         print("猜对了")
#         flag = False
#     elif gess_num < num:
#         print("小了")
#     elif gess_num > num:
#         print("大了")
# print("一共%d次"%(i))




# '''
# 99乘法表
# '''
# #定义外层循环的控制变量
# i = 1
# while i <= 9:
#
#     #定义内层循环的控制变量
#     j = 1
#     while j <= i:
#         #内层循环的print语句，不要换行
#         print(f"{j} * {i} = {j * i}\t",end="")    #通过制表符\t进行对齐
#         j += 1
#
#     i += 1
#     print()    #print()就是输出一个换行

# x = 'itheima is a brand of itcast'
# num = 0
# for m in x:
#     if m == 'a':
#         num +=1
# print(x + '中共含有：%d个字母a'%(num))


# i = 0
# num = int(input('请输入一个数：'))
# for x in range(1,num):
#     if x%2 == 0:
#         i += 1
# print(f'1到{num}(不含{num}本身)范围内，有{i}个偶数')



# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f"{i} * {j} = {j * i}\t",end="")
#     print()







