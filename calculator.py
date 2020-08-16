
def main():
	#write your code here
	n1 = input("Enter the first number: ")
	n1v = n1.isdigit()
	n2 = input("Enter the second number: ")
	n2v = n2.isdigit()
	oper = input("Choose the operation (+, -, /, *): ")
	if oper in ("+","-","/","*"):
		if n1v == True and n2v == True:
			if oper == "*" :
				print(int(n1) * int(n2))
			elif oper == "+" :
				print(int(n1) + int(n2))
			elif oper == "-" :
				print(int(n1) - int(n2))
			elif oper == "/" :
				if int(n2) == 0:
					print(" %s is invalid , %s deivded by zero is undefined" % (n2,n1))
				else: print(int(n1) / int(n2))
		else : print("number is invalid")
	else: print("operation is not valid")
		
			

	

	



if __name__ == '__main__':
	main()
