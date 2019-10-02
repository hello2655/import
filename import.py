import random

r = random.randint(1,100)

while True:
	num = input('請猜數字')
	num = int(num)
	if num == r:
		print('你猜中了！')
		break
	elif num > r:
		print('這個數字介於1至', num , '之間')
	elif num < r:
		print('這個數字介於', num ,'和100之間')