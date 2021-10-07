# Editor: GOTHIZzz
# Dev Date: 2021/10/7

# 模拟银行ATM输入密码取款的操作，错误的密码输入次数不超过3次，如果密码输入正确，直接结束for循环
for i in range(3):
    password = input('请输入密码：')
    if password == '123456':
        print('密码输入正确!')
        break
    else:
        print('密码输入错误!')


times = 0
while times < 3:
    password = input('请输入密码：')
    if password == '123456':
        print('密码输入正确!')
        break
    else:
        print('密码输入错误!')
        times += 1
