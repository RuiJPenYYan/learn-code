#encoding=gbk
#���е���Ӻ����
s1='hello'
s2='world'
s3='helloworld'

print(s1+s2)
print(s1*5)
print(s2*5)
print(s1 in s3)     #�ж��Ƿ����������
print(s3 in s1)
print(s1 in s1)
print('e��s1�д�����?',( 'e' in s1))
print('v��s1�в�������?',('v' not in s1))
print(s1.index('o'))  #s.index() �ҳ����һ�γ��ֵ�λ��
print(s3.count('l'))  #s.count() �ҳ�����ֵĴ���
print('max(s1)',max(s1))   #����ASCII����
print('min(s1)',min(s1))