# Editor: GOTHIZzz
# Dev Date: 2021/9/19
# 双分支 if...else，两个选择一个来执行
# 用键盘输入一个数字，用代码来判断这个数字是奇数还是偶数

number = int(input('请输入一个整数：'))

# 条件判断
if number % 2 == 0:
    print(number, '是一个偶数')
else:
    print(number, '是一个奇数')
    