from sys import argv

script, filename = argv # assign filename to argv[1]

txt = open(filename) # open file with filename

print(f"Here's your file {filename}:")
print(txt.read()) # print file content

print("Type the filename again:")
file_again = input("> ") # input filename again

txt_again = open(file_again) # open file again

print(txt_again.read()) # print file content