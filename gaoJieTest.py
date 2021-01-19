"""
author:Yuegb
date:2021,01,16
"""
# 映射
my_list1 = []
my_list2 = []
for i in range(1, 11):
    my_list1.append(i)
for i in range(11, 21):
    my_list2.append(i)
print(my_list1)
res = map(lambda x, y: x - y, my_list1, my_list2)
print(res)
print(list(res))

from functools import reduce

# reduce 规约
res = reduce(lambda x, y: x + y, my_list1)
print(list(range(1, 11)))
print(res)
print(sum(my_list1))
print(reduce(lambda x, y: x + y, range(1, 11), 11))  # 先加11

my_list = [1, 0, 0, 0, 1, 1]
# filter
res = filter(lambda x: True if x == 1 else False, my_list)
print(res)
print(list(res))
