"""
author:Yuegb
date:2021,01,16
"""
import time

# 三种时间表示：时间戳、结构化时间对象、格式化时间字符串
# 1
print(time.time())
# 2
st = time.localtime()
print(st)
print('today is {}-{:02}-{}'.format(st[0], st[1], st[2]))
print('today is week of: {}'.format(st.tm_wday + 1))
# 3
print('{0[4]} {0[1]} {0[2]} {0[3]}, {0[0]}'.format(tuple(time.ctime().split(' '))))
print(tuple(time.ctime().split(' ')))

# 4
print(time.strftime('今年是%Y年, 本周是第%W周'))

"""
for i in range(1,11):
    print(time.ctime())
    time.sleep(0.5)
"""
# 格式之间的转化
# 时间戳 -> 结构化对象 是UTC时间
print(time.gmtime(time.time() - 3600))
# 时间戳 -> local
print(time.localtime(time.time() - 3600))
# 结构化 -> 时间戳
print(time.time())
print(time.mktime(time.localtime()))

# 结构化 -> 格式化
print(time.strftime("%Y-%m", time.localtime()))

# 格式化 -> 结构化
geshi = time.strftime("%Y-%m", time.localtime())
print(time.strptime(geshi, "%Y-%m"))  # 缺少的小时等自动补齐
