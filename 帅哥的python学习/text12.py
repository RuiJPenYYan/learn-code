#encoding=gbk
#break在遍历循环中的使用
for i in 'helloworld!':
    if i=='!':
        break
    print(i,end='')
print()
print('-----------------------')

for i in range(3):
    user_name=input('请输入用户名:')
    pwd=input('请输入密码:')
    if user_name=='zl' and pwd=='123456':
        print('登入成功，请等待...')
        break
    else:
        if i<2:
            print('密码错误，你还有',2-i,'次机会')
    i+=1
else:  #for...else....
    print('三次均输入错误!')