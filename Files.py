helloFile = open ('/home/acoughlin/PycharmProjects/Learning/Helloworld.txt')
print (helloFile.read())

helloFile = open ('/home/acoughlin/PycharmProjects/Learning/Helloworld2.txt', 'w')
print (helloFile.write('Hello!!!!!!'))
helloFile.close()

import os
print (os.getcwd())

import shelve
shelfFile = shelve.open("mydata")
shelfFile["cats"] = ["Zophie", "Pooka", "Simon"]
shelfFile.close()

shelfFile = shelve.open("mydata")
print (shelfFile["cats"])


print(list(shelfFile.keys()))
print(list(shelfFile.values()))


# Section 11 32 - copy and move files

#import shutil
#shutil.copy('/home/acoughlin/PycharmProjects/Learning/Helloworld2.txt', '/home/acoughlin/PycharmProjects/helloworldtest.txt')
#shutil.move('/home/acoughlin/PycharmProjects/Learning/Helloworld2.txt', '/home/acoughlin/PycharmProjects')

# Section 11 22 - Deleting FIles

os.unlink('/home/acoughlin/PycharmProjects/Learning/Helloworld2.txt')
os.rmdir('/home/acoughlin/PycharmProjects/testfolder')