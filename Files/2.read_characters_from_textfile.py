# reading characters from file
# open the file for reading data

f = open('Files/myfile.txt', 'r') # to read data from the file. the file pointer is positioned at the beginning of the file.

# read all characters from file
str = f.read()

# display them on the screen 
print(str)

# closing the file
f.close()