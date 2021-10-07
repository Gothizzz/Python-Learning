# Editor: GOTHIZzz
# Dev Date: 2021/10/7
# 打印出三行四列的星型矩阵
# * * * *
# * * * *
# * * * *
for i in range(1,4):
    for j in range(1,5):
        print('*', end='\t')
    print()


# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()

