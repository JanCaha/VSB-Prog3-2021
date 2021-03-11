import re

regex_tel_number = re.compile(r"(\+?(00)?)?(420)?[0-9]{9}")

numbers = ["+420 123 578 897", "00420 125 247 578", "+420 123 21 54 76", "751 213 678"]

for number in numbers:

    number_fixed = re.sub(r"\s", "", number)
    print(re.sub(r"(\+?(00)?)?(420)?", "", number_fixed))

    r = regex_tel_number.match(number_fixed)

    if r:
        print(r.group(0))
        # print(r.group(1))
        # print(r.group(3))
