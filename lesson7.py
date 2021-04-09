file = open('text.txt', 'r')

print(file.read(1))
print()
print(file.read(1))
print()
print(file.read())
print()
print()

f = open('text.txt')

for line in f:
	print(line)