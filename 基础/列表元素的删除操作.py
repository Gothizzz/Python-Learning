# Editor: GOTHIZzz
# Dev Date: 2021/10/13
lst = [10, 20, 30, 40, 50, 60, 30]

lst.remove(30) # 默认删除首次出现的

print(lst)

lst.pop(1) # 根据索引来删

print(lst)

lst.pop() # 不指定索引，默认删除列表最后一个

print(lst)

lst[1:3] = [] # 删除列表索引1-3不包括3

print(lst)

lst.clear()

print(lst)