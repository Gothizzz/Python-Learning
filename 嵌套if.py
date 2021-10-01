# Editor: GOTHIZzz
# Dev Date: 2021/10/1
mystar = int(input('当前用户的星星数:'))
gender = input('当前用户的性别:')
#判断级别
if 0 < mystar <=20:
    if gender == 'boy':
        mystar += 1
    else:
        mystar += 2
print(mystar)