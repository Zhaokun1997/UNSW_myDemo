#Q2

def f(L,front_first=True):
	'''
	>>> L=[0,1,2,3,4,5]
	>>> front_first=True
	>>> f(L,front_first)
	[0, 5, 1, 4, 2, 3]
	>>> L=[0,1,2,3,4,5]
	>>> front_first=False
	>>> f(L,front_first)
	[5, 0, 4, 1, 3, 2]
	>>> L=[3,2,1,4,85,5]
	>>> front_first=True
	>>> f(L,front_first)
	[3, 5, 2, 85, 1, 4]
	>>> L=[3,2,1,4,85,5]
	>>> front_first=False
	>>> f(L,front_first)
	[5, 3, 85, 2, 4, 1]
	'''
	out_list=[]
	if front_first:
		for i in range(len(L)):
			if i % 2 == 0:
				out_list.append(L[i//2])
			else:
				out_list.append(L[-((i+1)//2)])
	else:
		for i in range(len(L)):
			if i % 2 == 0:
				out_list.append(L[-(i+2)//2])
			else:
				out_list.append(L[(i-1)//2])
	print(out_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')

