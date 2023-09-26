import os

directory = 'files'
filename = 'my_file_to_write.txt'
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, directory, filename)

try:
    with open(file_path, 'w', encoding='UTF-8') as file:
      file.write('Here is thw new content')
except FileNotFoundError:
    print(f"File not found: {file_path}")

except IOError as e:
    print(f"Error reading the file: {e}")
    
file.close()