#encoding=gbk
#����žų˷���
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print()
import random
rand=random.randint(1,100)  #����1-100֮��������������1��100
count=1
while count<=10:
    number=eval(input('����������һ����,1-100֮��,�����һ��:'))
    if number==rand:
        break
    elif number>rand:
        print('����,���²�:')
    else:
        print('С��,���²�:')
    count+=1
if count<=3:
    print('�����,һ������',count,'��')
elif count<=6:
    print('������,һ������',count,'��')
else:
    print('�µĴ����е��,һ������',count,'��')
