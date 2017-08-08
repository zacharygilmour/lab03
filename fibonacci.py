'''
Write a program that, given the index, will calculate
the n-th number in the fibonacci sequence.
The fibonacci sequence is defined as 
f(x) = 
	| x == 0     = 0
	| x == 1     = 1
	| otherwise  = f(x - 1) + f(x - 2)
The index is to be read from the standard input and 
the fibonacci number at that index is to be printed
to the standard output. You may assume that your
program will be tested with valid inputs only.
'''

index = input()


# Define this function to return the expected output
# Do not print it from this function
def fib_sequence(num):
	arrays_num = [0] * (num + 1)
	arrays_num[0] = 0
	arrays_num[1] = 1 
	if num > 1:
		for n in range(2, num):
			arrays_num[n] = arrays_num[n - 1] + arrays_num[n - 2]
	return arrays_num[index]
	pass

print(fib_sequence(index))
