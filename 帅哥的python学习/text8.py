#encoding=gbk
#(1)初始化变量
i=0
while i<3:   #条件判断
    #(3)语句块
    user_name=input('请输入你的用户名:')
    password=input('请输入你的密码:')
    #登陆操作 if...else...
    if user_name=='zl'and password=='123456':
        print('系统正在登陆中...')
        #(4)需要改变循环变量 跳出循环
        i=8  #退出循环
    else:
        if i<2:
            print('用户名或密码错误,您还有',2-i,'次机会')
        i+=1  #(4)改变变量
if i==3:
    print('错误次数过多')