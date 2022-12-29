from pathlib import Path
p1 = Path('files/abc.txt')
print(p1)

if p1.exists():
  with open(p1, 'r') as file:
    print(file.read())

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path('files')
for item in p2.iterdir():
  print(item, type(item))
  
