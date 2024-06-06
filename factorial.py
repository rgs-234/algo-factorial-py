
# # Recursive solution
# def factorial(num):
# 	if num == 2:
# 		return num
# 	else:
# 		return num * factorial(num - 1)
	

# Non-recursive solution
def factorial(num):
    result = 1
    
    for num in range(1, num + 1):
        result *= num
        
    return result