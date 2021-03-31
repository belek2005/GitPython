while True:
	def calculator():
		a = int(input("Введите первое число: "))
		b = int(input("Введите второе число: "))
		c = input("Введите оператор: ")
		if(c == "*"):
			print(a*b)
		elif(c == "+"):
			print(a+b)
		elif(c == "-"):
			print(a-b)
		elif(c == "/"):
			print(a/b)
		else:
			print("Неверный ввод")
	calculator()
