import FreeSimpleGUI as fsg
import functions as fxns

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter  todo", key= "todo",
                          size=([35, 5]))

add_btn = fsg.Button("Add")
list_box = fsg.Listbox( values=fxns.get_todos(),
                        key= 'todos',
                        enable_events=True,
                        size=[35, 15])

edit_btn = fsg.Button("Edit")
complete_btn = fsg.Button("Complete")

windows = fsg.Window("Your Favourite TODO App",
                      layout=[[label],
                              [input_box, add_btn],
                               [list_box, [edit_btn, complete_btn]]],
                        font= ('Helvetica', 15))

while True:
  event, value = windows.read()
  print(f"event ={event} \nvalue = {value}")

  match event:

    case "Add":
      todos = fxns.get_todos()
      new_todos = value['todo'] + "\n"
      todos.append(new_todos)
      fxns.write_todos(todos)
      windows['todos'].update(values=todos)
    case fsg.WIN_CLOSED:
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

windows.close()