# This code is for a todo app
user_prompt = input("Enter an an option below to continue")
print("""HINT
	Add --> To add a task
	Remove or Delete --> To delete a todo task
	Edit --> To edit the todo list
	Show or Display --> To show or display todo list
	Quit or Exit --> To quit or edit the todo
	Completed --> To mark a todo task as completed""")

while True:
	todo = input("Enter a a task to do")
	match user_prompt
