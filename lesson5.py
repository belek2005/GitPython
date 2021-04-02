def create_stack():
	return[]

def push(stack, element):
	stack.append(element)
	return stack


def is_empty(stack):
	if not stack:
		return True
	else:
		return False


def remove(stack):
	if not is_empty(stack):
		stack.pop()
	return stack

def calc(stack):
	i = 0
	while i < len(stack) - 1:
		yield stack[i] * stack[i + 1]
		i +=1
