import FreeSimpleGUI as fsg

label1 = fsg.Text("Select Files to compress")
input1 = fsg.Input()
choose_btn1 = fsg.FileBrowse("Choose")

label2 =fsg.Text("Select destination folder:")
input2 = fsg.Input()
choose_btn2 = fsg.FileBrowse("Choose")

comp_btn = fsg.Button("Compressor")

#input_box = fsg.InputText(tooltip="Enter  todo")
windows = fsg.Window("File Compressor",
                      layout=[[label1, input1, choose_btn1],
                               [label2, input2, choose_btn2],
                                 [comp_btn]])
windows.read()
windows.close()