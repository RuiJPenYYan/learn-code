#encoding=gbk
#(1)��ʼ������
i=0
while i<3:   #�����ж�
    #(3)����
    user_name=input('����������û���:')
    password=input('�������������:')
    #��½���� if...else...
    if user_name=='zl'and password=='123456':
        print('ϵͳ���ڵ�½��...')
        #(4)��Ҫ�ı�ѭ������ ����ѭ��
        i=8  #�˳�ѭ��
    else:
        if i<2:
            print('�û������������,������',2-i,'�λ���')
        i+=1  #(4)�ı����
if i==3:
    print('�����������')