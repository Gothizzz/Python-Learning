# Editor: GOTHIZzz
# Dev Date: 2022/1/26

# 小括号方式
t = ('James', '18', '180')
print(type(t))

# 省略小括号方式
y = 'James', '18', '180'
print(type(y))

# 只有一个元素需加逗号结束，不然为字符串
d =('James')
print(type(d))

d =('James',)
print(type(d))

# 使用tuple函数进行创建
c =tuple(('James', '18', '180'))
print(type(c))