"""
author:Yuegb
date:2021,01,16
"""


def add(x, y):
    return x + y


Lamb = lambda x, y: x + y

print(add('a', 'b'))
print(Lamb('a', 'b'))

# 与三目表达式结合使用

Lamb = lambda x, y: x if x > y else y
myList = [
    ('a', 1),
    ('b', 5),
    ('c', 4),
    ('d', 2),
]
print(sorted(myList, key=lambda x: x[1]))
print(myList)
