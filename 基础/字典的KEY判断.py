# Editor: GOTHIZzz
# Dev Date: 2022/1/4

# 判断是否在字典中
s = {'张星':100, 'James':101, '尅尅':99}
print('James' in s)
print('James' not in s)

# 删除字典中元素
del s['张星']
print(s)

# 字典新增
s['xxx']=60
print(s)

# 字典修改
s['James']=200
print(s)

# 清空字典
s.clear()
print(s)

