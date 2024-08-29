
<<<<<<< HEAD
To_delete = int(input("Enter the todo number yu want to delete: "))
Response = (input("Enter Yes or No to proceed: ")).capitalize()

if Response == "Yes":
    with open('todos.txt', 'r') as file:
        todos = file.readlines()

    todos.remove(todos[To_delete - 1])
            
    with open('todos.txt', 'w') as file:
        todos = file.writelines(todos)
        #print(f"{todos[To_edit]} succesfully edited to {New_todo}")
        
elif Response == "No":
    exit

else:
    print("Wrong command\nPlease enter 'YES' to delete or 'NO' to cancel deleting")
=======
with open('todos.txt', 'r') as file:
    todos = file.readlines()
print(todos)
>>>>>>> a7f0a12767ec81df89421e3dc5464bdc134baa55

with open('todos.txt', 'r') as file:
    todos = file.readlines()
print(todos)