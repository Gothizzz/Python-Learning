# Editor: GOTHIZzz
# Dev Date: 2021/10/13
lst = [10, 45, 28, 32, 12, 5]
print('未排序之前的数据：', lst)

lst.sort() # 默认按升序排序，不打乱内存地址

print('排序之后的数据：', lst)

# 通过一些关键字排序
lst.sort(reverse=True) # 降序

print(lst)

# 内置函数进行排序
lst = [10, 45, 28, 32, 12, 5]
print('未排序之前的数据：', lst)

lst2 = sorted(lst)

print('排序之后的数据：', lst2)

lst2 = sorted(lst, reverse=True) # 降序

print('排序之后的数据：', lst2)


