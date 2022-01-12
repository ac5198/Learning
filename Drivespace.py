current = float(input('What is the current drive size in GB? '))
free = (float(input('How much free space is left on the drive in GB? ')))
percent = (float(input('What percent do you want free? ')))

convertpercent = (percent / 100)
used = (current - free)
newpercent = (1 - convertpercent)
newsize = (used / newpercent)

print ('\nThe new drive size will need to be ', round(newsize), 'GB')

add = (newsize - current)
print ('You will need to add an additional ', round(add), 'GB')

k=input("\npress enter to exit")346.5
