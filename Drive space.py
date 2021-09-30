# Ask for drive size
print ('What is the current drive size in GB?')
current = (int(input()))

# Ask for free space
print ('How much free space is left on the drive in GB?')
free = (int(input()))

# Ask for amount free space wanted
print ('What percent do you want free')
percent = (float(input()))
convertpercent = (percent / 100)

#Calculate used space
used = (current - free)
print (used)

#Calculate desired drive size
newpercent = (1 - convertpercent)
newsize = (used / newpercent)
print ('The new drive size will need to be ', newsize, ' GB')

#Calculate how much to add
add = (newsize - current)
print ('You will need to add an additional ', add, 'GB')
