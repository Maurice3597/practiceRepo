# This code is for a todo Program

print("""		HINT
	Add --> To add a task
	Remove or Delete --> To delete a todo task
	Edit --> To edit the todo list
	Show or Display --> To show or display todo list
	Quit or Exit --> To quit or edit the todo
	Completed --> To mark a todo task as completed\n""")

while True:
	user_action = (input("Enter an option here to continue: ")).lower()#+ "\n"
	match user_action:
		case "add":
			todo = input("Add a TODO task: ") + "\t"
			
			file = open('todos.txt', 'r')
			todos = file.readlines()
			file.close()

			todos.append(todo)

			file = open('todos.txt', 'w')
			file.writelines(todos)
			file.close()
			#just trying to see if the right todo list will be printed out
			for i, j in enumerate(todos):
				row = f"{i+1}-{j}"
				print(row)
		
		case "edit":
			todo = input("Enter the Todo you want too edit: ") + "\n"
			New_todo = input("Enter the new Todo: ")

			file = open('todos.txt', 'r')
			todos = file.readlines()
			file.close()

			if todo in todos:
				todos.remove(todo)
				todos.append(New_todo)
				file = open('todos.txt', 'w')
				file.writelines(todos)
				file.close()
				for i, j in enumerate(todos):
					row = f"{i+1}-{j}"
					print(row)
			else:
				print(f"MISMATCH!!\nSorry couldn't find {todo} in the TODO list")

		case "remove" | "Delete":
			todo = input("Enter the TODO task you want to delete or remove: ")
			
			file = open('todos.txt', 'r')
			todos = file.readlines()
			file.close()

			if todo in todos:
				todos.remove(todo)
				print(f"{todo} removed from list")
			else:
				print(f"Couldn't find {todo} in the TODO list")

		case "show" | "display":
			file = open('todos.txt', r)
			todos = file.readlines()
			file.close()



		case "complete" | "done":
			todo = input("Enter the TODO task you have completed: ")
			if todo in todos:
				todos = todos.remove(todo)
			
				print(f"{todo} completed and removed from list")
			else:
				print(f"Sorry can't find {todo} in the todos list")

		case "quit" | "exit":
			break

		case _:
			print("Sorry, you typed the wrong command\nSee the hint for the right commands")


