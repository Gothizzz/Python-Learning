# Editor: GOTHIZzz
# Dev Date: 2021/10/13
lst = [10, 20, 30]

print('添加新元素前的数据：',lst)

lst.append(100) # 追加到列表的最右侧末尾

print('添加新元素后的数据：',lst)

lst2 = ['hello', 'james']

lst.append(lst2) # 将lst2整体追加到lst后

print(lst)

lst.extend(lst2) # 平级追加

print(lst)

# 在列表的任意位置添加一个元素
lst.insert(2, 90)

print(lst)