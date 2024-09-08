import FreeSimpleGUI as fsg
import functions as fxns
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'x'):
        pass

fsg.theme('Black2')
clock = fsg.Text("", key="clock")
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter  todo", key= "todo",
                          size=(35, 2))

add_btn = fsg.Button("Add", size= 5)
list_box = fsg.Listbox( values=fxns.get_todos(),
                        key= 'todos',
                        enable_events=True,
                        size=(35, 10))

edit_btn = fsg.Button("Edit", size= 4)
complete_btn = fsg.Button("Complete")
clear_btn = fsg.Button("Clear", size= 5)
exit_btn = fsg.Button("Exit", size= 4)

windows = fsg.Window("Your Favourite TODO App",
                      layout=[[clock],[label],
                              [input_box, add_btn],
                               [list_box, edit_btn, complete_btn], [clear_btn, exit_btn]],
                        font= ('Helvetica', 15))

while True:
  event, value = windows.read(timeout=500)
  windows['clock'].update(value= time.strftime("Date: %d-%b-%y  %I:%M:%S %p"))

  match event:

    case "Add":
      todos = fxns.get_todos()
      new_todo = value['todo'] + "\n"

      if new_todo =='' + "\n":
          fsg.popup("Please Enter a TODO first",
                    title="Error Message",
                    font= ('Helvetica', 15))
      else:
          todos.append(new_todo)
          fxns.write_todos(todos)
          windows['todos'].update(values=todos)
          windows['todo'].update(value="")

    case fsg.WIN_CLOSED | "Exit":
      break

    case "todos":
        windows['todo'].update(value = value['todos'][0])

    case "Edit":
        try:
          todos_to_edit = value['todos'][0]
          new_todo = value['todo']

          todos = fxns.get_todos()
          index = todos.index(todos_to_edit)
          todos[index] = new_todo
          fxns.write_todos(todos)
          windows['todos'].update(values=todos)
          windows['todo'].update(value="")
        except IndexError:
            fsg.popup("No todo Selected‼️\nSelect a todo and try again",
                      title="ERROR 🚫⛔",
                      font= ('Helvetica', 15))

    case "Complete":
        try:
            todo_completed = value['todos'][0]
            todos = fxns.get_todos()
            todos.remove(todo_completed)
            fxns.write_todos(todos)
            windows['todos'].update(values=todos)
            windows['todo'].update(value='')
        except IndexError:
            fsg.popup("No todo Selected‼️\nSelect a todo and try again",
                      title="ERROR 🚫⛔",
                      font= ('Helvetica', 15))
    case "Clear":
        todos = fxns.get_todos()
        todos.clear()
        fxns.write_todos(todos)
        windows["todos"].update(values={})

   # case "Exit":
    #  break

windows.close()