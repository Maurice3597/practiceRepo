# This code is for a todo Program
#from practice.functions import file_path

print("""		HINT
	Add --> To add a task
	Remove or Delete --> To delete a todo task
	Edit --> To edit the todo list
	Show or Display --> To show or display todo list
	Quit or Exit --> To quit or edit the todo
	Completed --> To mark a todo task as completed\n""")

#

#file_path = 'todos.txt'

# def get_todos(filepath):
#    with open(filepath, 'r') as local_file:
#        local_todos = local_file.readlines()
#    return local_todos


#ef write_todos(todo_arg, filepath):
#    with open(filepath, 'w') as local_file:
#       local_file.writelines(todo_arg)

import functions
while True:
    user_prompt = ((input("Enter a Todo:\n")).lower()).lstrip()
    
    if user_prompt.startswith("add"):
        todo = (user_prompt[4:]).lstrip() + "\n"
        todos = functions.get_todos("todos.txt")

        todos.append(todo)

        functions.write_todos(todos, "todos.txt")
        print(f"\"{todo}\" Successfully added to the the TODO list")
        
    elif user_prompt.startswith("edit"):
        New_todo = (user_prompt[4:]).lstrip() + "\n"
        To_edit = int(input("Enter the number you want to edit: "))
        
        todos = functions.get_todos("todos.txt")

        print(f"Are you sure you want to edit \"{todos[To_edit]}\" ??\n")
        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            todos = functions.get_todos("todos.txt")

            todos[To_edit - 1] = New_todo
            
            functions.write_todos(todos, "todos.txt")
                #print(f"{todos[To_edit]} successfully edited to {New_todo}") This a bug to be debugged in a later version
        
        elif Response == "No":
            exit("Edit successfully cancelled")

        else:
            print("Wrong command\nPlease enter 'YES' to edit or 'NO' to cancel editing")

    elif user_prompt.startswith("show"):
        todos = functions.get_todos("todos.txt")

        todos = [item.strip('\n') for item in todos]
        for position, task in enumerate(todos):
            print(f"{position + 1}- {task}")
        
    elif user_prompt.startswith("delete"):
        To_delete = int(input("Enter the todo number you want to delete: "))

        todos = functions.get_todos("todos.txt")

        print(f"Are you sure you want to delete \"{todos[To_delete - 1]}\" ??\n:")

        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            todos = functions.get_todos("todos.txt")

            todos.remove(todos[To_delete - 1])
            
            functions.write_todos(todos, "todos.txt")
                #print(f"{todos[To_edit]} successfully edited to {New_todo}")
        
        elif Response == "No":
            exit ("Delete successfully cancelled")
            
        else:
            print("Wrong command\nPlease enter 'YES' to delete or 'NO' to cancel deleting")

    elif user_prompt.startswith("completed"):
        Completed = int(input("Enter the todo number you want to mark as completed: "))

        todos = functions.get_todos("todos.txt")

        print(f"Are you sure you want to mark \"{todos[Completed - 1]}\" as completed??\n"
              "Note that this action will also delete the completed task from the list:")

        Response = (input("Enter Yes or No to proceed: ")).capitalize()

        if Response == "Yes":
            todos = functions.get_todos("todos.txt")

            todos.remove(todos[Completed - 1])
            
            functions.write_todos(todos, "todos.txt")
            
            print(f"\"{todos[Completed - 1]}\" completed successfully and removed from the list")
        
        elif Response == "No":
            exit ("Mark complete cancelled")
            
        else:
            print("Wrong command\nPlease enter 'YES' to approve task as completed or 'NO' to cancel")

    else:
        break
