# Editor: GOTHIZzz
# Dev Date: 2022/1/28

# 集合与字典的区别
# 字典（为key-value）
a = {'James':180, 'Jack':181, 'Peter':182}
print(type(a))

# 集合
b = {1, 1, 2, 3, 5, 8}
print(type(b))

# set()的方法来创建集合
c = set(range(7))
print(c)

# 自动去掉重复的元素
d = set((1, 2, 3, 4, 4, 4, 5))
print(d)

# 分割字符串(无序）
e = set('James')
print(e, type(e))