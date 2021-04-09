l = [str(i) + str(i-1) for i in range(20)]

f = open('test_1.txt', 'w')

for i in l:
	f.write(i + "\n")

f.close()

f = open('test.txt', 'r')

print(f.readline())
print(f.tell())
f.seek(1)
print(f.read(10))
# l = [line.strip() for line in f]
# print(l)