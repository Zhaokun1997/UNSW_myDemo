#Q6
def f(word):
	'''
	>>> word='abcabcdf'
	>>> f(word)
	abcd
	>>> word='dsfopqrsbsdfabcdfasd'
	>>> f(word)
	opqrs
	>>> word='abcddfbuvwxyccc'
	>>> f(word)
	uvwxy
	'''
	longest_length= 0
	start=0
	current_start=0
	while len(word)-longest_length > current_start:
		current_length= 1
		for i in range(current_start+1,len(word)):
			if ord(word[i]) - ord(word[i-1])==1:
				current_length+=1
				current_start+=1
			else:
				break
		if current_length > longest_length:
			longest_length=current_length
			start=current_start - longest_length+1
		current_start+=1
	print(''.join(chr(ord(word[start])+i) for i in range(longest_length)))
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
