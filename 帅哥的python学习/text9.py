#encoding=gbk
print('长方形:')
#外层循环
for i in range(1,4):
    #内层循环
    for j in range(1,5):
        print('*',end='') #end=''让他不自动换行
    print() #print空语句的作用是换行
print('---------------------------')
print('直角三角形:')
for i in range(1,6):  #5行
    #*的个数与行相同，range(1,2),第二行，range(1,3)
    for j in range(1,i+1):
        print('*',end='')
    print() #换行
print('---------------------------')
print('倒三角形:')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()
print('---------------------------')
print('等腰三角形:')
'''
&&&*       2    4
&&***      4    3    
&*****     6    2
*******    8    1         12-2i
'''
for i in range(1,6):
    #打印倒三角形空格
    for j in range(1,6-i):
        print(' ',end='')
    #1,3,5,7...等腰三角形
    for k in range(1,2*i):
        print('*',end='')
    print()#两个内循环都结束时执行换行

print('---------------------------')
print('菱形:')
for i in range(1,6):
    #打印倒三角形空格
    for j in range(1,6-i):
        print(' ',end='')
    #1,3,5,7...等腰三角形
    for k in range(1,2*i):
        print('*',end='')
    print()#两个内循环都结束时执行换行
for i in range(1,6):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,10-2*i):
        print('*',end='')    
    print()