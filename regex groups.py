import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search("My number is 785-330-3346")
mo = phoneNumRegex.search("My number is 785-330-3346")
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 785-330-3346")
print(mo.group())

print(mo.group(1))
print(mo.group(2))


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('The Batmobile lost a wheel')
print(mo.group())