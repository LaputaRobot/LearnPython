"""
author: Yuegb
date:2021,01,15
"""


class Cat:
    """
    this is a class named Cat
    """
    className = "ketty"

    def __init__(self, name, age=0):
        self.name = name
        self.__color = "white"
        self.age = age

    def __del__(self):
        print("del {}".format(str(self.name)))

    def __call__(self, *args, **kwargs):
        print(args[0] + args[1])

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        return iter(self.__dict__)

    def __getitem__(self, key):
        if key == 'name':
            return self.name
        else:
            return None

    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
        else:
            self.key = value

    def __delitem__(self, key):
        if key == 'name':
            del self.name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            print("other is subjected to the class of self")
            return [self.name, other.name]
        elif isinstance(other, list):
            other.append(self.name)
            return other


cat = Cat('ketty')
cat1 = Cat('mimi', 1)
cat2 = Cat('lily')
print("attr:" + cat.name)
print("doc:" + cat.__doc__)
print("module name:" + cat.__module__)
print("class name:" + str(cat.__class__))
cat(1, 8)
print(cat.__dict__)
print("name length:", len(cat))
print("cat的实例属性一共有：", end='')
for i in cat:
    print(i, end=';')
print()
print(cat.__getattribute__('name'))
print(cat['name'])
cat['name'] = 'sweet'
print(cat['name'])
del cat['name']
cat['name'] = 'ketty'  # 可以为删除的属性再次赋值
# cat['age'] = 1 不能使用该方法为实例添加属性
# print(cat.age)
# print(cat.name)
cats = cat + cat1
print(cats)
print(cat2 + cats)

