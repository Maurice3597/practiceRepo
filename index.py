# This code is for a todo Program

print("""		HINT
	Add --> To add a task
	Remove or Delete --> To delete a todo task
	Edit --> To edit the todo list
	Show or Display --> To show or display todo list
	Quit or Exit --> To quit or edit the todo
	Completed --> To mark a todo task as completed\n""")

while True:
    user_prompt = ((input("Enter a Todo:\n")).lower()).lstrip()
    
    if user_prompt.startswith("add"):
        todo = (user_prompt[4:]).lstrip() + "\n"
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            
        todos.append(todo)
        with open('todos.txt','w') as file:
            file.writelines(todos)
        print(f"\"{todo}\" Successfully added to the the TODO list")
        
    elif user_prompt.startswith("edit"):
        New_todo = (user_prompt[4:]).lstrip() + "\n"
        To_edit = int(input("Enter the number you want to edit: "))
        
        with open('todos.txt', 'r') as file:
                todos = file.readlines()

        print(f"Are you sure you want to edit \"{todos[To_edit]}\" ??\n")
        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos[To_edit - 1] = New_todo
            
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
                #print(f"{todos[To_edit]} succesfully edited to {New_todo}") This a bug to be debugged in a later version
        
        elif Response == "No":
            exit("Edit succesfully cancelled")

        else:
            print("Wrong command\nPlease enter 'YES' to edit or 'NO' to cancel editing")

    elif user_prompt.startswith("show"):
        with open('todos.txt') as file:
            todos = file.readlines()

        todos = [item.strip('\n') for item in todos]
        for position, task in enumerate(todos):
            print(f"{position + 1}- {task}")
        
    elif user_prompt.startswith("delete"):
        To_delete = int(input("Enter the todo number you want to delete: "))

        with open('todos.txt') as file:
            todos = file.readlines()

        print(f"Are you sure you want to delete \"{todos[To_delete - 1]}\" ??\n:")

        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.remove(todos[To_delete - 1])
            
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
                #print(f"{todos[To_edit]} successully edited to {New_todo}")
        
        elif Response == "No":
            exit ("Delete successfully cancelled")
            
        else:
            print("Wrong command\nPlease enter 'YES' to delete or 'NO' to cancel deleting")

    elif user_prompt.startswith("completed"):
        Completed = int(input("Enter the todo number you want to mark as completed: "))

        with open('todos.txt') as file:
            todos = file.readlines()

        print(f"Are you sure you want to mark \"{todos[Completed - 1]}\" as completed??\n"
              "Note that this action will also delete the completed task from the list:")

        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.remove(todos[Completed - 1])
            
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
            print(f"\"{todos[Completed - 1]}\" completed successfully and removed from the list")
        
        elif Response == "No":
            exit ("Mark complete cancelled")
            
        else:
            print("Wrong command\nPlease enter 'YES' to approve task as completed or 'NO' to cancel")

    else:
        break
