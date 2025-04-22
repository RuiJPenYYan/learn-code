fp=open('note.txt','w') # 打开文件w-->write
print('python',end='',file=fp) #将其输入(写入)到文件note.txt中
# +号将字符串和字符串连接在一起
# end=是结束符
fp.close #关闭文件