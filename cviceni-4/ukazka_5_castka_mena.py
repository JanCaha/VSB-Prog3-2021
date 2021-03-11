import re


def convert_to_USD(amount: float, from_type: str) -> float:
    if from_type == "$":
        return amount
    elif from_type == "£":
        return amount * 1.25
    elif from_type == "¥":
        return amount / 1000
    else:
        raise ValueError("Unknown money type!")


incomes = ["50.5 $", " 1£", "1000,10¥", "0$ ", "5 CZK"]

incomes = [x.strip() for x in incomes]

print(incomes)

regex = re.compile(r"(\d+[.|,]?\d*)\s?([$£¥]{1})")

for income in incomes:

    r = regex.match(income)

    if r:
        number = float(r.group(1).replace(",", "."))
        type = r.group(2)

        number_USD = convert_to_USD(number, type)

        print(f"The income is {number:.2f} in {type}. Which is {number_USD:.2f} in $.")
