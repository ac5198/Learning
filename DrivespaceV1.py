# Ask for drive size
current = int(input('What is the current drive size in GB? '))

# Ask for free space
free = (int(input('How much free space is left on the drive in GB? ')))

# Ask for amount free space wanted
percent = (float(input('What percent do you want free? ')))
convertpercent = (percent / 100)

#Calculate used space
used = (current - free)

print(' ')

#Calculate desired drive size
newpercent = (1 - convertpercent)
newsize = (used / newpercent)
print ('The new drive size will need to be ', newsize, ' GB')

#Calculate how much to add
add = (newsize - current)
print ('You will need to add an additional ', add, 'GB')

print(' ')

k=input("press enter to exit")

