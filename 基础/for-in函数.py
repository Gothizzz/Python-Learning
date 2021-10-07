# Editor: GOTHIZzz
# Dev Date: 2021/10/7
# while 0:
#     print('hello world')

for str in 'James':
    print(str)

for i in range(10):
    print(i)

# 循环体中没有变量，可以用_来代替
for _ in range(10):
    print('James')

# 用for循环来计算0-10之间的偶数的和
sum = 0
for i in range(10):
    if i%2 == 0:
        sum = sum + i
print(sum)