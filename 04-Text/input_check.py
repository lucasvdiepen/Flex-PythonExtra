import re

while True:
    phone = input("Voer je mobiele nummer in: ")

    patroon = r"^06-?\d{8}$"

    matches = re.findall(patroon, phone)

    if(len(matches) > 0):
        break

print("Bedant nummer in juiste formaat: " + matches[0])
