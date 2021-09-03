#read the file and split it into tokens
filename = "input.txt"
file_handle = open(filename)
text = file_handle.read()
file_handle.close()

words = text.split()
#make all words lowercase for consistency
tokens = [word.lower() for word in words]

print(tokens)

