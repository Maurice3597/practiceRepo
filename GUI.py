import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter  todo")
add_button =fsg.Button("Add")
windows = fsg.Window("Your Favourite TODO App", layout=[[label], [input_box, add_button]])
windows.read()
windows.close()