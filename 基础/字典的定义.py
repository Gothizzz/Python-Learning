# Editor: GOTHIZzz
# Dev Date: 2022/1/3

# 使用{}创建字典
s = {'张星':100, 'James':101, '尅尅':99}
print(s)

order = {'订单号':10032, '时间':20210908, '数量':2, '金额':99}
print(order)
print(type(order))

# 第二种方式
order = dict(订单号=10032, 时间=20210908)
print(order)

# 空的字典
d = {}
print(d)