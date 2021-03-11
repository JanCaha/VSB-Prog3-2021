import re

text = "00420 587 15 62\t34"

text = re.sub(r"\s", "", text)

print(text)

r = re.match(r"(\+?(00)?){1}420[0-9]{9}", text)

print(r)
print(r.group(0))
