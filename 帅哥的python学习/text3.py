#ecoding=gbk
luck_number = 8

my_name = '����'

print('luck_number��������:',type(luck_number))
print('my_name��������:',type(my_name))

#��̬�������͵�ת��
luck_number = 'ͬ�ܱ�Ů'
nice = '������'
print('luck_number��������:',type(luck_number))

#��python��֧�ֶ������ָ��ͬһ��ֵ
no=number=1024  #no��number��ָ����1024�������ֵ
print(no)
print(number)
print('---------------�ָ���-----------------')
print(id(no))
print(id(number))

pi = 3.1415926 #����
PI = 3.1415926 #����

#����ȫ�ô�д��ĸ

#Ĭ��Ϊʮ���Ʋ���Ҫ��������
# ������ 0b��0B(��������)
# �˽��� 0o��0O
# ʮ������ 0x��0X
num=978
num2=0b111101
num3=0o56771
num4=0x565A
print(num,num2,num3,num4)
print('---------------�ָ���-----------------')
print(0.1+0.2) #���Ϊ0.30000000000000004    ��ȷ������������

print(round(0.1+0.2,1))   # 1 ����˼�Ǳ���һλС��

x=123+456j #�������͵ı�ʾ���� 
print(x.real) #ʵ������
print(x.imag) #��������
print('-----------------------------')
print('��������')
print('\'��������\'')
print('����\t����')
print(r'����\t����')   # r��R��ʹת���ַ�ʧЧ

s='helloworld'
print(s[0],s[-10])  #��� 0 �� -10 ��ͬһ���ַ���
m='ɽ����ѽ'
print(m[0],m[-4])
print(s[2:7])  #��2��ʼ��7����������7
print(m[0:4])

print(luck_number+nice)  #���������ַ���
print(luck_number*10)   #������ַ�������10��
print('������'in luck_number)
print('������'in nice)
# x in s
#���xΪs���Ӵ� ��Ϊtrue����Ϊfalse

