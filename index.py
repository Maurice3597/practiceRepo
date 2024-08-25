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
        print(f"{todo}Successfully added to the the TODO list")
        
    elif user_prompt.startswith("edit"):
        New_todo = (user_prompt[4:]).lstrip() + "\n"
        To_edit = int(input("Enter the number you want to edit: "))
        
        with open('todos.txt', 'r') as file:
                todos = file.readlines()

        print(f"Are you sure you want to edit {todos[To_edit]}??\n")
        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos[To_edit] = New_todo
            
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
                print(f"{todos[To_edit]} succesfully edited to {New_todo}")
        
        elif Response == "No":
            exit

        else:
            print("Wrong command")

    else:
        break