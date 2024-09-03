import FreeSimpleGUI as fsg
import functions as fxns


label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter  todo", key= "todo")
add_button =fsg.Button("Add")

windows = fsg.Window("Your Favourite TODO App",
                      layout=[[label], [input_box, add_button]],
                        font= ('Helvetica', 15))

while True:
  print(windows.read())
  event, value = windows.read()

  match event:

    case "Add":
      todos = fxns.get_todos()
      new_todos = value['todo'] + "\n"
      todos.append(new_todos)
      fxns.write_todos(todos)
    case fsg.WIN_CLOSED:
      break

windows.close()