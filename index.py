# This code is for a todo Program

print("""		HINT
	Add --> To add a task
	Remove or Delete --> To delete a todo task
	Edit --> To edit the todo list
	Show or Display --> To show or display todo list
	Quit or Exit --> To quit or edit the todo
	Completed --> To mark a todo task as completed\n""")

todos =[]
while True:
	user_action = (input("Enter an option here to continue: ")).lower()#+ "\n"
	match user_action:
		case "add":
			todo = input("Add a TODO task: ") + "\t"
			todos.append(todo)
			file = open('todos.txt', 'w')
			file.writelines(todos)
			file.close()
			for i, j in enumerate(todos):
				row = f"{i+1}-{j}"
				print(row)
		
		case "edit":
			""

		case "remove" | "Delete":
			todo = input("Enter the TODO task you want to delete or remove: ")
			print(f"{todo} removed from list")

		case "show" | "display":
			""

		case "complete" | "done":
			todo = input("Enter the TODO task you have completed: ")
			todos = todos.remove(todo)
			print(f"{todo} completed and removed from list")
		case "quit" | "exit":
			break

		case _:
			print("Sorry, you typed the wrong command\nSee the hint for the right commands")


#This code produces the multiplication table for any chosen number
n = int(input("Enter the number whose multiplication table you're looking for: "))
print(f"\nThe multiplcation table for {n} is\n")
for i in range(1, 13):
    print(f"{n} x {i} = {n * i} \n")
print("Hello World\n")

multiples =[]
for k in range(1,101):
    if k % 3 == 0:
        multiples.append(k)
print(F" {multiples} is a list of multiple of 3")
