#encoding=gbk
#ģ��10086������ѯƽ̨
print('----------��ӭ����10086������ѯƽ̨----------')
while True:
    print('1.��ѯ��ǰ���')
    print('2.��ѯ��ǰʣ������')
    print('3.��ѯ��ǰʣ��ͨ��ʱ��')
    print('0.�˳���ǰ����')
    choice=eval(input('������Ҫ���еķ���:'))
    if choice==1:
        yuan=35
        print('��ǰ�����Ϊ',yuan,'Ԫ')
        a=input('�찡,���������,�Ƿ���г�ֵ:y/n')
        if a=='y':
            money=eval(input('������Ҫ��ֵ�Ľ��'))
            print('��ֵ�ɹ�,��Ҳ̫��ʵ����')
            print('��ǰ���Ϊ:',yuan+money)
            print('����Ҫ����ʲô����:')
            continue
        else:
            continue
    elif choice==2:
        print('��ǰʣ������Ϊ:176GB')
        print('����Ҫ����ʲô����:')
        continue
    elif choice==3:
        print('��ǰʣ��ͨ��ʱ��Ϊ:175����')
        print('����Ҫ����ʲô����:')
        continue
    elif choice==0:
        print('���������˳�,лл���ʹ��!��!')
        break
    elif choice==10086:
        print('�յ�,���ڼ��ظ��ӷ���,������������')
    else:
        print('��������,����������:')
        continue   