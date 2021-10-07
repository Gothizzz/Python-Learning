# Editor: GOTHIZzz
# Dev Date: 2021/10/7
# break 与 continue 在二重循环中的应用
for i in range(5):
    for j in range(1,11):
        if j%2 == 0:
            continue
        print(j,end='\t')
    print()