# Editor: GOTHIZzz
# Dev Date: 2021/9/19

a, b = 25.8, 25.7

print('a大于b吗？', a > b)

print('a不等于b吗？', a != b)

# 输入一个=表示右边的值传递给左边，输入两个==对比左右是否相等
# a变量：标识，类型，值
# a == b来对比，比较的是值
# a和b的标识地址是否相等，is

a, b = 20, 20

print(a is b)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]

print(l1 == l2)
print(l1 is l2)
print(id(l1), id(l2))