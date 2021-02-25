from pathlib import Path

p = Path(__file__)

print(p.name)
print(p.stem)
print(p.suffix)
print(p.absolute())
print(p.relative_to(p.parent))
print(p.relative_to(p.parent.parent))

print("-" * 60)

for file in p.parent.iterdir():
    print(file)

folder = p.parent

print(folder)
print(type(folder))

non_existing_folder = folder / "a_folder"

print(non_existing_folder)
print(non_existing_folder.exists())

non_existing_folder.mkdir()

print(non_existing_folder.exists())

non_existing_folder.rmdir()

print(non_existing_folder.exists())
