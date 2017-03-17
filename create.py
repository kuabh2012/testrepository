import os, sys, stat

#Enter directory name to be created.
dirname = raw_input('Enter directory name: ')

#Create the directory from the input.
os.mkdir(dirname)

#Create sub directories and set permissions.
os.mkdir(dirname + "/SubdirLevel1")
os.mkdir(dirname + "/SubdirLevel1/SubdirLevel2")
os.chown(dirname + "/SubdirLevel1/SubdirLevel2", 777, 777)
os.chmod(dirname + "/SubdirLevel1/SubdirLevel2", stat.S_IRWXO)

print('The directory ' + dirname + " has been created.")