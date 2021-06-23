class Stack:
  def __init__(stack_name):
    stack_name.items = []

  def isEmpty(stack_name):
    if not stack_name:
      return True
    else:
      return False

  def push(stack_name, elem):
    stack_name.items.append(elem)

  def remove(stack_name):
    if not stack_name:
      return stack_name
    else:
      return stack_name.items.pop()

  def calc(stack_name):
    if 1 < len(stack_name.items):
      i = 0
      while i < len(stack_name.items) - 1:
        yield stack_name.items[i] * stack_name.items[i + 1]
        i += 1
    else:
      return stack_name
