# try:
# 	for i in range(3):
# 		print(3/i)

# except:
# 	print("Деление на 0")
# 	print("Исключение было обработано")

# a, b = 1, 0
# try:
# 	print(a/b)
# 	print("это не будет напечатано")
# 	print('10' + 10)
# except TypeError:
# 	print("Вы сложили значения несовместимых типов")
# except ZeroDivisionError:
# 	print("Деление на 0")

# try:
# 	print("10" + 10)
# 	print(1/0)

# except (TypeError, ZeroDivisionError):
# 	print("Неверный ввод")

# try:
# 	print("1" + 1)
# 	print(sum)
# 	print(1/0)

# except ZeroDivisionError:
# 	print("Деление на 0")

# except NameError:
# 	print("Sum не существует")

# except:
# 	print("Что то пошло не так")

# try:
# 	print("2")

# print("3")
# except:
# 	print("4")

# try:
# 	print(1/0)
# except:
# 	raise
# except:
# 	print("Ошибка найдена")
# finally:
# 	print("Хорошо")
# print("Пока")
# try:
# 	print(1/0)
# except ValueError:
# 	print("Mistake found")
# finally:
# 	print("This will write in other situations")

# try:
# 	print(1/0)
# except ZeroDivisionError:
# 	print(2/0)
# finally:
# 	print("This will write in other situations")

# a, b = int(input("Write first num: ")), int(input("Write second num: "))
# try:
# 	if b == 0:
# 		raise ZeroDivisionError	
# except:
# 	print("Wrong delenie")
# print("Will it write?")		

try:
	print("1" + 1)
except:
	raise TypeError("Можно складывать лишь строки со строками, а не строки с числами!")