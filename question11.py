"""Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?"""


filename = input("Enter filename along with extensions: ")

splitFilename = filename.split('.')

print("The name of file without extension is ", splitFilename[0])
print("The extension in file is ", '.'+ splitFilename[1])