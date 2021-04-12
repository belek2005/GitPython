file = [str(10) + str(10) for l in range(100)]

f = open('test.txt', 'w')

for l in file:
	f.write("loremIpsum" + '\n')

f.close()

f = open('test.txt', 'r')

print(f.read(10))
print(f.read(12))
print(f.read(11))
print(f.read(10))
print(f.read(11))
