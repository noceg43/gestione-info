# this will open the file
file = open('file.txt', encoding='utf8')
read = file.read()
file.seek(0)
read

# to obtain the
# number of lines
# in file
line = 1
for word in read:
	if word == '\n':
		line += 1
print("Number of lines in file is: ", line)

# create a list to
# store each line as
# an element of list
array = []
for i in range(line):
	array.append(file.readline())

print(array)
