# Editor: GOTHIZzz
# Dev Date: 2021/10/7
# 银行卡输入密码，错误密码超过3次
# for循环
# for i in range(3):
#     pwd = input('请输入密码：')
#     if pwd == '666666':
#         print('密码输入正确！')
#         break
#     else:
#         print('密码输入错误！')
# else:
#     print('输入超过三次！')

# while循环
i = 0
while i < 3:
    pwd = input('请输入密码：')
    if pwd == '666666':
        print('密码输入正确！')
        break
    else:
        print('密码输入错误！')
        i += 1
else:
    print('输入超过三次！')