#Q3
from math import sqrt
from collections import defaultdict
def f(number):
	'''
	>>> f(6889091714695477660879872)        #number== 2^10 * 3^2 * 941^2 * 947^3 * 997^2
	5330721714
	'''
	prime_factor=defaultdict(int)
	v=number
	while v > 1:
		l, remainder = divmod(v,2)
		if remainder:
			break
		else:
			v = l
			prime_factor[2]+=1
	for i in range(3,int(sqrt(number))+1,2):
		while v > 1:
			l, remainder = divmod(v, i)
			if remainder:
				break
			else:
				v=l
				prime_factor[i]+=1
		else:
			break
	product=1
	for i in prime_factor.keys():
		product*=i
	return product

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
