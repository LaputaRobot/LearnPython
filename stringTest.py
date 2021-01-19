"""
author:Yuegb
date:2021,01,15
"""
# 字符串格式化输出：%s
# %的使用：叫做占位符
print("string is :%s" % 'hello')
s = 'hello'
t = '20210115'
print("string is :%s" % s)
# 格式：%[-][+][0][m][.n]格式化字符 %参数
temp = 'string is: % s'
print(temp % s)
# m 占位宽度 +-：对齐方式 .字符串截取 0：补0
temp = 'string is: |%20s|'
temp_ = 'string is: |%-20s|'
tempDian = 'string is: |%.3s|'
tempDouble = 'string is: |%20s|%s|'
print(temp % s)
print(temp_ % s)
print(tempDian % s)
print(tempDouble % (s, t))

# %d 十进制 %x 十六进制 %o 八进制
template_10 = 'number is: |%010d|'
template_16 = 'number is: |%+010x|'
template_8 = 'number is: |%-10o|'
templateFloat = 'number is: |%-10f|'  # 默认有6位小数
templateFloatDian = 'number is: |%10.3f|' # 四舍五入？
print(template_10 % 23)
print(template_16 % 0x3d)
print(template_8 % 0o23)
print(templateFloat % 1.2345)
print(templateFloatDian% 1.2345)

# 金额的千分位表示
print(temp% format(12344.5, ','))
