import re

while True:
    invoer = input("Voer je kenteken in: ")

    patroon = r"^[A-Z]{2}-\d{3}-[A-Z]{3}$"
    matches = re.findall(patroon, invoer)

    if(len(matches) > 0):
        break

print("Bedankt kenteken in juiste formaat: " + matches[0])
