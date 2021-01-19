"""
author:Yuegb
date:2021,01,16
"""
import datetime
import time

# 生成日期
d = datetime.date.today()
print(d, type(d))
d = datetime.date(2020, 1, 1)
print(d, type(d))
d = datetime.date.fromtimestamp(time.time())
print(d, type(d))

# 类的属性
print(datetime.date.max)
print(datetime.date.min)
print(datetime.date.resolution)

# 实例属性
print(d.day)
print(d.month)
print(d.year)

# datetime.date -> 结构化时间
print(d.timetuple())
# 替换
print(d)
print(d.replace(d.year, 9))
print(d.replace(month=9))
print(d.weekday())  # 0代表周一
print(d.isoweekday())  # 0代表周天
print(d.isoformat())
print(d.strftime("%Y-%m"))

# -------------------------------------------------------
print('-'*50)
t = datetime.time(15, 8, 55, 8)
print(t, type(t))

# 类方法
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

# 实例属性
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# 其他方法
print(t.isoformat())
print(t.strftime("%M分%S秒"))

# ***************************************************
print('*'*50)
dt = datetime.datetime.fromtimestamp(time.time())
print(dt)
dt = datetime.datetime(2021, 1,16)
print(dt)
dt = datetime.datetime.strptime("2021-1-16","%Y-%m-%d")
print(dt)
dt = datetime.datetime.combine(d,t)
print(dt)

# 属性、replace与上述类似
# 转换
print(dt.timetuple())
print(dt.timestamp())
print(dt.strftime("%Y-%m"))

# 时间差
td = datetime.timedelta(10)
print(td,type(td))

# 时间差的使用
dt = datetime.datetime.today()
print(f"现在是：{dt}")
print("十天后是：{}".format(dt + td))

