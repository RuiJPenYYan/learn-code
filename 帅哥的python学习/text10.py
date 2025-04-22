#encoding=gbk
row=eval(input('请输入菱形的行数:'))
while row%2==0:  #判断行数是否为偶数，为偶数重新输入行数
    print('请重新输入行数，不能为偶数')
    row=eval(input('请输入菱形的行数:'))

#--------输出菱形---------
top_row=(row+1)//2 #上半部分行数
#上半部分
for i in range(1,top_row+1):
    #打印倒三角形空格
    for j in range(1,top_row+1-i):
        print(' ',end='')
    #1,3,5,7...等腰三角形
    for k in range(1,2*i):
        print('*',end='')
    print()#两个内循环都结束时执行换行

bottom_row=row//2  #下半部分行数
#下半部分
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):  # 1-->range(1,8)   2-->range(1,6)  
        print('*',end='')    
    print()
print('-----------------------------------')
#-----------打印空心菱形--------------
top_row=(row+1)//2 #上半部分行数
#上半部分
for i in range(1,top_row+1):
    #打印倒三角形空格
    for j in range(1,top_row+1-i):
        print(' ',end='')
    #1,3,5,7...等腰三角形
    for k in range(1,2*i):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()#两个内循环都结束时执行换行

bottom_row=row//2  #下半部分行数
#下半部分
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):  # 1-->range(1,8)   2-->range(1,6)  
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')
        else:
            print(' ',end='')   
    print()