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
