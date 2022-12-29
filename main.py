from pathlib import Path

# Using pathlib to find, create files
# p1 = Path('files/abc.txt')
# print(p1)

# if p1.exists():
#   with open(p1, 'r') as file:
#     print(file.read())

# print(p1.name)
# print(p1.stem)
# print(p1.suffix)

# p2 = Path('files')
# for item in p2.iterdir():
#   print(item, type(item))
  
# Using pathlib to manipulate files - adding prefix to all filenames in folder
# root_dir = Path('files')
# file_paths = root_dir.iterdir()
# # print(list(file_paths))

# for path in file_paths:
#   new_filename = "new-" + path.stem + path.suffix
#   new_filepath = path.with_name(new_filename)
#   path.rename(new_filepath)

# Rename all files based on folder

root_dir = Path('files')
# file_paths = root_dir.iterdir()
# Elegant way to go in file folders and thus escaping the nested "for-loop" below
file_paths = root_dir.glob("**/*")

for path in file_paths:
  if path.is_file():
    parent_folder = path.parts[-2]
    new_filename = parent_folder + "-" + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
  