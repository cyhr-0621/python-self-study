from datetime import datetime #引用datetime库
now = datetime.now() #获得当前日期和时间信息
print(now)
now.strftime("%x") #输入其中的日期部分
now.strftime("%x") #输入其中的时间部分

#日期和时间的输出