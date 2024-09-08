import FreeSimpleGUI as fsg
from FreeSimpleGUI import theme_element_text_color

from archive_Ext_Function import extract_archive

label1 = fsg.Text("Select Archive:")
input1 = fsg.Input()
filebtn = fsg.FileBrowse('Choose', key='archive')

label2 =fsg.Text('Select Dest. folder')
input2 = fsg.Input()
folder_btn = fsg.FolderBrowse('Choose', key='folder')

Extract_btn = fsg.Button("Extract", key='extract')
output_label = fsg.Text(key="output", text_color='green')
exit_btn = fsg.Button('Exit', key='Exit')

window = fsg.Window("ARCHIVE EXTRACTOR",
                     layout = [[label1, input1, filebtn],
                              [label2, input2, folder_btn],
                              [Extract_btn, output_label, exit_btn]],
                    font= ('Helvetica', 15))

while True:
    event, values = window.read()
    print(event, values)
    archived_path = values['archive']
    dest_folder = values['folder']

    match event:
        case 'fsg.WIN_CLOSED' | 'Exit':
            break
        case 'extract':
            extract_archive(archived_path, dest_folder)
            output_label.update(value= 'Extraction Successful.')

window.close()