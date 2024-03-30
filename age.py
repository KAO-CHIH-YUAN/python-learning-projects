driving = input('有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('輸入錯誤了喔')
	raise SystemExit

age = int(input('請問你的年齡?'))
if driving == '有':
	if age >= 18:
		print('通過測驗了')
	else:
		print('奇怪 你有開過車???')
elif driving == '沒有':
	if age >= 18:
		print('可考駕照喔')
	else:
		print('請成年後再來')