
def main():
	#write your code here
	n1 = input("Enter the first number: ")
	while not n1.isdigit():
		print(" %s is invalid" % n1)
		n1 = input("Enter the first number: ")
	n2 = input("Enter the second number: ")
	while not n2.isdigit():
		print(" %s is invalid" % n2)
		n2 = input("Enter the second number: ")
	oper = input("Choose the operation (+, -, /, *): ")
	while oper not in ("+","-","/","*"):
		print(" %s is invalid" % oper)
		oper = input("Choose the operation (+, -, /, *): ")


	if oper == "*" :
		print(int(n1) * int(n2))
	if oper == "+" :
		print(int(n1) + int(n2))
	if oper == "-" :
		print(int(n1) - int(n2))
	if oper == "/" :
		if int(n2) == 0:
			print(" %s is invalid , %s deivded by zero is undefined" % (n2,n1))
		else: print(int(n1) / int(n2))
			

	

	



if __name__ == '__main__':
	main()
