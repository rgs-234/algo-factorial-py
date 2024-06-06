def factorial(num):
	if num == 2:
		return num
	else:
		return num * factorial(num - 1)