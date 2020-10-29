import re
import sys
import os.path

if(len(sys.argv) > 1):
    f = sys.argv[1]
    if(not os.path.isfile(f)):
       print("Bestand niet gevonden")
       exit()
else:
    while True:
        invoer = input("In welk bestand wil je zoeken: ")
        f = invoer.strip()

        if(os.path.isfile(f)): break
        else: print("Bestand niet gevonden\n")

emails = []
google_emails = []

print("")

with open(f, "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        patroon = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z-0-9_-]+"
        google_patroon = r"[a-zA-Z0-9._-]+@gmail\.com"

        gevonden = re.findall(patroon, regel)

        google_emails_gevonden = re.findall(google_patroon, regel)

        if(len(gevonden) > 0):
            emails.extend(gevonden)

        if(len(google_emails_gevonden) > 0):
            google_emails.extend(google_emails_gevonden)
        
        regel = bestand.readline()

print("Alle email adressen: ")
print(emails)
print("\nAlle google email adressen: ")
print(google_emails)

email_list = "\n".join([str(email) for email in emails])
google_email_list = "\n".join([str(email) for email in google_emails])

#write to files
emails_file = open("alle_emails.txt", "w")
emails_file.write(email_list)
emails_file.close()

google_emails_file = open("google_emails.txt", "w")
google_emails_file.write(google_email_list)
google_emails_file.close()

input("\n\n\nDruk enter om dit te sluiten")
