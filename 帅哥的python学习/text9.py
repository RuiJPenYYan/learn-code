#encoding=gbk
print('������:')
#���ѭ��
for i in range(1,4):
    #�ڲ�ѭ��
    for j in range(1,5):
        print('*',end='') #end=''�������Զ�����
    print() #print�����������ǻ���
print('---------------------------')
print('ֱ��������:')
for i in range(1,6):  #5��
    #*�ĸ���������ͬ��range(1,2),�ڶ��У�range(1,3)
    for j in range(1,i+1):
        print('*',end='')
    print() #����
print('---------------------------')
print('��������:')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()
print('---------------------------')
print('����������:')
'''
&&&*       2    4
&&***      4    3    
&*****     6    2
*******    8    1         12-2i
'''
for i in range(1,6):
    #��ӡ�������οո�
    for j in range(1,6-i):
        print(' ',end='')
    #1,3,5,7...����������
    for k in range(1,2*i):
        print('*',end='')
    print()#������ѭ��������ʱִ�л���

print('---------------------------')
print('����:')
for i in range(1,6):
    #��ӡ�������οո�
    for j in range(1,6-i):
        print(' ',end='')
    #1,3,5,7...����������
    for k in range(1,2*i):
        print('*',end='')
    print()#������ѭ��������ʱִ�л���
for i in range(1,6):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,10-2*i):
        print('*',end='')    
    print()