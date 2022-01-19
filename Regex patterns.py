import re

# ? can appear zero or one times

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The adventures of Batwoman")
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The adventures of Batman")
print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search("My phone number is 785-330-3346")
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search("My phone number is 330-3346")
print(mo.group())

# * can appear zero or unlimited times

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("The adventures of Batwowowoman")
print(mo.group())

# + can appear one or more times

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search("The adventures of Batwowowoman")
print(mo.group())

# \* to search for a *

regex = re.compile(r'\+\*\?')
mo = regex.search("I learned about +*? syntax")
print(mo.group())

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search("He said 'HaHaHa'")
print(mo.group())

# greedy match by default

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search("He said 'HaHaHaHa'")
print(mo.group())

# ? makes it a non greedy match

haRegex = re.compile(r'(Ha){3,5}?')
mo = haRegex.search("He said 'HaHaHaHa'")
print(mo.group())