texts = ["5", "5a", "a", "5.1"]

for text in texts:
    print(f"isalnum() for variable {text} is {text.isalnum()}")
    print(f"isdigit() for variable {text} is {text.isdigit()}")
    print(f"isdecimal() for variable {text} is {text.isdecimal()}")
    print(f"isalpha() for variable {text} is {text.isalpha()}")

text = "tento text bude rozdělen podle mezer ale\tne\tpodle\ttabulátorů"

result = text.split(" ")

print(result)

print(text.title())

print(text.endswith("átorů"))
print(text.endswith("x"))
