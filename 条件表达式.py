# Editor: GOTHIZzz
# Dev Date: 2021/10/1
a = int(input('请输入一个整数：'))
b = int(input('请输入另一个整数：'))

# if a >= b:
#     print(a,'大于或等于',b)
# else:
#     print(a,'大于',b)

print(str(a)+'大于或等于'+str(b) if a >= b  else str(a)+'小于'+str(b))
