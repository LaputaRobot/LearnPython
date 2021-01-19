"""
author:Yuegb
date:2021,01,15
"""
"""

format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

template = '格式化的内容为： {} {}'
print(template.format('hello', 12))

# index
print("{0} {1} {1}".format(1, 2))

# s 字符串
print("{:s}".format('hello'))
print("|{:20}|".format('hello'))  # 默认左对齐
print("|{:20.2s}|".format('hello'))
print("|{:*>20s}|".format('hello'))
print("|{:+^20s}|".format('hello'))

# 数值
print("|{:20d}|".format(123))  # 默认右对齐
print("|{:+^20d}|".format(123))
print("|{0:*>5d}|{0:*>5x}|{0:*>#5x}|".format(123))

# 数值 + - ' '
print("|{:d}|{:d}|".format(13, -23))
print("|{:+d}|{:+d}|".format(13, -23))
print("|{:-d}|{:-d}|".format(13, -23))
print("|{: d}|{: d}|".format(13, -23))

# 浮点数 略

# 参数的传递
print("{name} {age}".format(name='ketty', age=2))
number = (1, 2, 3)
dic = {'name':'ketty','age':2}
print("{0[0]} {0[1]} {0[2]}".format(number))
print("{0[name]} {0[age]}".format(dic))

# 千分位
print("{:,f}".format(123456.34))
print("{:_d}".format(123456))
