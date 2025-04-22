#encoding=gbk
#模拟10086自助查询平台
print('----------欢迎进入10086自助查询平台----------')
while True:
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余通话时长')
    print('0.退出当前服务')
    choice=eval(input('请输入要进行的服务:'))
    if choice==1:
        yuan=35
        print('当前的余额为',yuan,'元')
        a=input('天啊,你真是穷逼,是否进行充值:y/n')
        if a=='y':
            money=eval(input('请输入要充值的金额'))
            print('充值成功,你也太有实力辣')
            print('当前余额为:',yuan+money)
            print('还需要进行什么服务:')
            continue
        else:
            continue
    elif choice==2:
        print('当前剩余流量为:176GB')
        print('还需要进行什么服务:')
        continue
    elif choice==3:
        print('当前剩余通话时长为:175分钟')
        print('还需要进行什么服务:')
        continue
    elif choice==0:
        print('程序正在退出,谢谢你的使用!喵!')
        break
    elif choice==10086:
        print('收到,正在加载附加服务,喵！！！！！')
    else:
        print('输入有误,请重新输入:')
        continue   