# Creating a file to store Characters
# Open the file for writing data
f = open('Files/myfile.txt','w') # w means it would be deleted and the present data will be stored.

# enter characters from keyboard
str = input('Enter the Message : ')

# write the string into file
f.write(str)

# closing the file
f.close()