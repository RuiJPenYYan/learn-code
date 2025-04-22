#encoding=gbk
d={'hello':10,'math':20,'python':30}
#访问字典元素
#(1)
print(d['hello'])
#(2)
print(d.get('hello'))

#如果key不存在,d[]会报错,d.get()可以指定默认值
#print(d['java'])
#KeyError: 'java'
print(d.get('java'))
print(d.get('java','不存在'))

#字典的遍历
for item in d.items():
    print(item)

for key,value in d.items():
    print(key,'--->',value)