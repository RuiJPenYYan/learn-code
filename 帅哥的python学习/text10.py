#encoding=gbk
row=eval(input('���������ε�����:'))
while row%2==0:  #�ж������Ƿ�Ϊż����Ϊż��������������
    print('��������������������Ϊż��')
    row=eval(input('���������ε�����:'))

#--------�������---------
top_row=(row+1)//2 #�ϰ벿������
#�ϰ벿��
for i in range(1,top_row+1):
    #��ӡ�������οո�
    for j in range(1,top_row+1-i):
        print(' ',end='')
    #1,3,5,7...����������
    for k in range(1,2*i):
        print('*',end='')
    print()#������ѭ��������ʱִ�л���

bottom_row=row//2  #�°벿������
#�°벿��
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):  # 1-->range(1,8)   2-->range(1,6)  
        print('*',end='')    
    print()
print('-----------------------------------')
#-----------��ӡ��������--------------
top_row=(row+1)//2 #�ϰ벿������
#�ϰ벿��
for i in range(1,top_row+1):
    #��ӡ�������οո�
    for j in range(1,top_row+1-i):
        print(' ',end='')
    #1,3,5,7...����������
    for k in range(1,2*i):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()#������ѭ��������ʱִ�л���

bottom_row=row//2  #�°벿������
#�°벿��
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):  # 1-->range(1,8)   2-->range(1,6)  
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')
        else:
            print(' ',end='')   
    print()