filenames = {"file1t.xt": "This is file 1", "file2.txt" : "This is file 2","file3.txt" :"This is file3", "file4.txt" :  "This is file4"}

for filename, content in filenames.items():
    with open(filename, 'w') as file:
        file.write(content)