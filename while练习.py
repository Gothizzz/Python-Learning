# Editor: GOTHIZzz
# Dev Date: 2021/10/1

# 计算0到100中偶数的和
sum = 0
a = 0

while a <= 100:
     if a%2 == 0:
        sum = sum + a
     a += 1
print('偶数的和为：',sum)
