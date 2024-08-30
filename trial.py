
import functions

filepath = "todos.txt"
while True:
    user_action = input("enter a todo here: ") + "\n"

    todos = functions.get_todos(filepath)
    todos.append(user_action)
    functions.write_todos(todos, "todos.txt" )
    print(todos)