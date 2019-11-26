#Q7]
solutions=[]
def solve(available_digits, desired_sum):
	if desired_sum < 0:
		return 0
	if available_digits == 0:
		if desired_sum == 0:
			return 1
		return 0
	return solve(available_digits//10,desired_sum)+solve(available_digits//10,desired_sum-available_digits%10)
m=solve(1234,6)		
print(m)		
#这题不会
