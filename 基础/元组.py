# Editor: GOTHIZzz
# Dev Date: 2022/1/26

# Python内置的数据结构之一，是一个不可变序列

# 可变序列
lst = [1,2,3,4]
print(id(lst))
lst.append(5)
print(lst)
print(id(lst)) # id值未变

# 不可变序列
str = 'hello'
print(id(str))
str = str + 'hello'
print(id(str))
print(str)  # id值变化，表示原来的str已不存在

