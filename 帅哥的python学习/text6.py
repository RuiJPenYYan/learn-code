#encoding=gbk
number=eval(input('请输入你的六位中奖号码:'))
if number==987654:
    print('你中奖了')
else:
    print('你没中奖')
print('------------------------------')
result='你中奖了'if number==987654 else '你没中奖'
print(result)
print('你中奖了'if number==987654 else '你没中奖')