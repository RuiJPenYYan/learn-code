#encoding=gbk
#break�ڱ���ѭ���е�ʹ��
for i in 'helloworld!':
    if i=='!':
        break
    print(i,end='')
print()
print('-----------------------')

for i in range(3):
    user_name=input('�������û���:')
    pwd=input('����������:')
    if user_name=='zl' and pwd=='123456':
        print('����ɹ�����ȴ�...')
        break
    else:
        if i<2:
            print('��������㻹��',2-i,'�λ���')
    i+=1
else:  #for...else....
    print('���ξ��������!')