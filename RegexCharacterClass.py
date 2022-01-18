import re

resume = """
Functional Resume Sample
John W. Smith
2002 Front Range Way Fort Collins, CO 80525
jwsmith@colostate.edu
785-330-3346
918-845-3147
Career Summary
Four years experience in early childhood development with a diverse background in the care of
special needs children and adults.
Adult Care Experience
• Determined work placement for 150 special needs adult clients.
• Maintained client databases and records.
• Coordinated client contact with local health care professionals on a monthly basis.
• Managed 25 volunteer workers.
Childcare Experience
• Coordinated service assignments for 20 part-time counselors and 100 client families.
• Oversaw daily activity and outing planning for 100 clients.
• Assisted families of special needs clients with researching financial assistance and
healthcare.
• Assisted teachers with managing daily classroom activities.
• Oversaw daily and special student activities.
Employment History
1999-2002 Counseling Supervisor, The Wesley Center, Little Rock, Arkansas.
1997-1999 Client Specialist, Rainbow Special Care Center, Little Rock, Arkansas
1996-1997 Teacher’s Assistant, Cowell Elementary, Conway, Arkansas
Education
University of Arkansas at Little Rock, Little Rock, AR
• BS in Early Childhood Development (1999)
• BA in Elementary Education (1998)
• GPA (4.0 Scale): Early Childhood Development – 3.8, Elementary Education – 3.5,
Overall 3.4.
• Dean’s List, Chancellor’s List
"""
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(resume))

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

lyrics = "12 drummers drumming, 11 pipers piping, " \
         "10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, " \
         "7 swans a-swimming, 6 geese a-laying, 5 golden rings, " \
         "4 calling birds, 3 French hens 2 turtle-doves, " \
         "And 1 partridge in a pear tree"

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# making a character class

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall("Robocop eats baby food."))

vowelRegex = re.compile(r'[aeiou]{2}')
print(vowelRegex.findall("Robocop eats baby food."))

# ^ makes it opposite

consonatesRegex = re.compile(r'[^aeiou]')
print(consonatesRegex.findall("Robocop eats baby food."))

# starts with

beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search("Hello there!")
print(mo.group())

# ends with

endsWithHelloRegex = re.compile(r'world!$')
mo = endsWithHelloRegex.search("Hello world!")
print(mo.group())

allDigitesRegex = re.compile(r'^\d+$')
mo = allDigitesRegex.search("01892507896")
print(mo.group())

# . stands for any character

atRegex = re.compile(r'.at')
mo = atRegex.search("The cat with the hat is fat")
print(mo.group())