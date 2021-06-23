def create_stack():
  return []

def push(element, stack_name):
  stack_name.append(element)

def is_empty(stack_name):
  if stack_name == True:
    return True
  else:
    return False
def remove(stack_name):
  stack_name.pop()

def calc(stack_name):
  i = 0
  while i < len(stack_name) - 1:
    yield stack_name[i] * stack_name[i + 1]
    i += 1
