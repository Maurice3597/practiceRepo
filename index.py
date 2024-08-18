# This code is for a todo Program

print("""HINT
	Add --> To add a task
	Remove or Delete --> To delete a todo task
	Edit --> To edit the todo list
	Show or Display --> To show or display todo list
	Quit or Exit --> To quit or edit the todo
	Completed --> To mark a todo task as completed""")

user_prompt = input("Enter an an option below to continue")

while True:
	todo = input("Enter a a task to do")
	match user_prompt:
		case "add":
			todo = input("Add a TODO task")
			file = ('todos.txt' , 'w')
			todos = file.write(todo)
			file.close()
		
		case "edit":

		case "remove" | "Delete":
			todo = input("Enter the TODO task you want to delete or remove: ")
			print(f"{todo} removed from list")

		case "show" | "display":

		case "complete" | "done":
			todo = input("Enter the TODO task you have completed: ")
			todos = todos.remove(todo)
			print(f"{todo} completed and removed from list")
		case "quit" | "exit":
			break

		case _:
			print("Sorry, you typed the wrong command\nSee the hint for the right commands")

