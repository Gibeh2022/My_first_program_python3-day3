from sys import argv
# read the WYSS section for the how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
      Alright, so you said {likes} about liking me.
      You live in {lives}. Not sure where that is.
      And you have {computer} computer. Nice
      """)

from sys import argv

# read the filename
script, filename = argv  
# to open the file
txt = open(filename)
#print and format the file 
print(f"Here's your file {filename}:")
#called the function of txt nameed read
print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("if you dont want that, hit CTRL-C (^C).")
print("if you do want that, hit return.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file, Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()


from sys import argv
from os.path import exists

script, from_file, to_file, = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The inout file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL_C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()





