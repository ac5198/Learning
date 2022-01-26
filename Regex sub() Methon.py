import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))

print(namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob."))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))

# \1 only grabs text from group 1 (\w)

print(namesRegex.sub(r"Agent \1****", "Agent Alice gave the secret documents to Agent Bob."))

verboseRegex = re.compile(r'''
(\d\d\d-)|     # area code (without parens, with parent)
(\(\d\d\d\))   # -or- area code (with parens, no dash)
\d\d\d         # first 3 digits
-              # second dash
\d\d\d\d       # last 4 digits
\sx\d{2,4}     # extension, like x1234''', re.VERBOSE)

print(verboseRegex.findall("My phone number is 785-330-3346"))