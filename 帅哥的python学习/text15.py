#encoding=gbk
#输入一个年份，判断是否是闰年
#判断条件为能被4整除，但不能被100整除，或者能被400整除
year = eval(input('请输入年份：'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,'是闰年')
else:
    print(year,'是平年')