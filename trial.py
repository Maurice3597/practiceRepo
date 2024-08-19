file = open('todos.txt', 'r')
todos = file.readlines()
file.close()
file.close()
for item in todos:
	print(item)
print(len(todos))
print(todos[0])