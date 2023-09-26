import os

directory = 'files'
filename = 'my_file.txt'
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, directory, filename)

try:
    with open(file_path, 'r', encoding='UTF-8') as file:
        # Read the entire content of the file
        # content = file.read()
        content_lines = file.readlines()

        # Alternatively, you can read the file line by line using a loop
        # for line in file:
        #     print(line)

        # Do something with the content of the file
        # print(content)
        print(content_lines[2])

except FileNotFoundError:
    print(f"File not found: {file_path}")

except IOError as e:
    print(f"Error reading the file: {e}")
    
file.close()