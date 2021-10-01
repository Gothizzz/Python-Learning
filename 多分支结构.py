# Editor: GOTHIZzz
# Dev Date: 2021/9/19

mystar = int(input('当前用户的星星数:'))
#判断级别
if 0 < mystar <= 10:
    print(mystar,'当前等级为青铜')
elif 10 < mystar <= 30:
    print(mystar,'当前等级为白银')
elif 30 < mystar <= 50:
    print(mystar,'当前等级为黄金')
elif 50 < mystar <= 70:
    print(mystar,'当前等级为白金')
elif 70 < mystar <= 90:
    print(mystar,'当前等级为钻石')
elif 90 < mystar <= 110:
    print(mystar,'当前等级为王者')
else:
    print(mystar,'不在范围内')