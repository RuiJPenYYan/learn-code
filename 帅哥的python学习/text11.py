#encoding=gbk
print('-------------------------')
i=0 #ͳ������
while i<3:
    user_name=input('�������û���:')
    pwd=input('����������:')
    if user_name=='zl' and pwd=='123456':
        print('����ɹ�����ȴ�...')
        break
    else:
        if i<2:
            print('��������㻹��',2-i,'�λ���')
    i+=1
else:
    print('���ξ��������!')