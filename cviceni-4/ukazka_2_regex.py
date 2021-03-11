import re

text = "tento text bude rozdělen podle mezer ale\tne\tpodle\ttabulátorů"

r = re.findall(r"t[\S]+", text)

print(r)

text = "přidání před gray něco přidám grey"

r = re.search(r"gr[a|e]y", text)

print(r)

if r:
    print(r.group(0))

r = re.match(r"gr[a|e]y", text)

print(r)

if r:
    print(r.group(0))
