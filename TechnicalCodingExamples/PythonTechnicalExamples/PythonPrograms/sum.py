def getinput():
	try:
		num = int(input("Please enter your number for addition : "))
	except ValueError:
		print("Please enter onely integer values")
		getinput()
	else:
		return num

def getinput2():
	try:
		num1 = int(input("Please enter your 2nd number for addition : "))
	except:
		print("Please enter onely integer values")
		getinput2()
	else:
		return num1
def caladd():
	a = getinput()
	b = getinput2()
	a = a + b
	print("Addition of two values is : ",a)

def main():
	caladd()
	input()
if __name__ == "__main__":
	main()