#encoding=gbk
#����һ����ݣ��ж��Ƿ�������
#�ж�����Ϊ�ܱ�4�����������ܱ�100�����������ܱ�400����
year = eval(input('��������ݣ�'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'������')
else:
    print(year,'��ƽ��')