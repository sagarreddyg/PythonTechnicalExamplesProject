# Sum of Two User given Numbers with out any exceptions
def caladd():
	try:
		a = int(input("Enter your First Integer value : "))
		b = int(input("Enter your Second Integer value : "))
		c = a + b
		print("Sum of {} and {} is : {}".format(a, b, c))
	except ValueError:
		caladd()


def main():
	caladd()
	input()


if __name__ == "__main__":
	main()
