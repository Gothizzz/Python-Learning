# Editor: GOTHIZzz
# Dev Date: 2021/10/1
x = [1,2,3,4,5]
print(list(x))
# range怎么用
r = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 从0开始，产出数据到10，不包括10，间隔为1（间隔=步长）
print(list(r))

# 给个开始的起步的参数1
r = range(1,10)
print(list(r))

# 给个开始的起步的参数2，步长为2
r = range(2,20,2)
print(list(r))

print(2 in r)
print(3 in r)
