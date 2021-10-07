# Editor: GOTHIZzz
# Dev Date: 2021/10/7
# 输出1-20之间，哪些是5的倍数，5，10，15，20
# 除以5后取余数，看余数是否为0，说明是5的倍数

for i in range(1,21):
    if i%5 == 0:
        print(i)

# continue语句
for i in range(1,21):
    if i%5 != 0:
        continue
    print(i)