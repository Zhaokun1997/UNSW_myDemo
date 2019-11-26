#Q4
def f(width,height):
	'''
	>>> f(17,4)
	abcdefghijklmnopq
	hgfedcbazyxwvutsr
	ijklmnopqrstuvwxy
	ponmlkjihgfedcbaz
	>>> f(2,2)
	ab
	dc
	>>> f(5,4)
	abcde
	jihgf
	klmno
	tsrqp
	'''
	start = 0
	chr_list=[[] for i in range(height)]
	for index,line in enumerate(chr_list):
		for i in range(width):
			line.append(chr(97+(start+i)%26))
		if index % 2 ==1:
			line.reverse() 
		start+=width
	for i in chr_list:
		print(''.join(i))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
