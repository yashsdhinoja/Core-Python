# creating the file with string
# open the file from writing the data

f = open('Files/group of strings.txt','w')

print("Enter the (/ at end) : ")

while str != '/':
    str = input()
    if(str != '/'):
        f.write(str+"\n")

f.close()