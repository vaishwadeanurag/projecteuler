def main():
	one = 1
	two = 2
	total = 2
	while True:
		fib = one + two
		if fib % 2 == 0:
			total += fib
		one , two = two , fib
		if fib >= 4000000:
			break
	print total

if __name__ == '__main__':
	main()