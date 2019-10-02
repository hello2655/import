import random

s = input('請輸入開始值')
e = input('請輸入結束值')
s = int(s)
e = int(e)

r = random.randint(s,e)
count = 0

while True:
	count = count + 1
	num = input('請猜數字')
	num = int(num)
	print('這是第', count , '次')
	if num == r:
		print('你猜中了！')
		break
	elif num > r:
		print('這個數字介於', s ,'和', num , '之間')
	elif num < r:
		print('這個數字介於', num ,'和', e ,'之間')
