import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?  #area code (optional)
(\s|-)                      # first seperator
\d\d\d                      # first 3 digits
-                           # seperator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
(\d{2,5}))?                 # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+             # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
#text = pyperclip.paste()
#print(text)
text = """Jessie Mckay jmckay67@aol.com 479-205-4874
Tom Jordan tjordan@msn.com 678-560-3485
Clayton Cross ccross20@gmail.com 724-900-2986
Rayford Sutton rayfords66@hotmail.com 242-391-3183
Jerome Gentry jgentry@me.com 604-720-6426
Weldon Camacho wcamacho57@icloud.com 651-807-8065
Quinton Franks qfranks@comcast.net 209-754-9111
Adam Hubbard cygzfjd61@outlook.com 641-433-6698"""

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

print(results)