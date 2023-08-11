height = input('请问您的身高是： (单位：cm)')
height = float(height)
height = height / 100
weight = input('请问您的体重是： (单位：kg)')
weight = float(weight)
bmi = weight/height**2
if bmi <= 18.5:
	print('您的bmi指数为： ', bmi, '您的体重过轻')
elif bmi <= 25:
	print('您的bmi指数为： ', bmi, '您的体重正常')
elif bmi <= 35:
	print('您的bmi指数为： ', bmi, '您的体重轻度肥胖')
elif bmi <= 40:
	print('您的bmi指数为： ', bmi, '您的体重中度肥胖')
else:
	print('您的bmi指数为： ', bmi, '您的体重重度肥胖')