# Write code that asks the user for their name, then opens a file called "name.txt"
# and writes that name to it. Remember to close your file.

name = input("what is your name?")
out_file = open("names.txt", "w")
print(f"{name}", file = out_file)
out_file.close()

# (In the same file, but as if it were a separate program)
# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

in_file = open("names.txt", "r")
print(f"your name is {in_file.readline()}")
out_file.close()

# Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400

number_file_write = open("numbers.txt", "w")
numbers = [17, 42, 400]
for i in range(0, len(numbers)):
    print(f"{numbers[i]}", file=number_file_write)
number_file_write.close()

# Write code that opens "numbers.txt", reads only the first two numbers and adds them
# together then prints the result, which should be... 59.

number_file_read = open("numbers.txt", "r")
numbers = number_file_read.readlines()[0:2]
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
print(f"result is: {sum(numbers)}")
number_file_read.close()

# Now write a fourth block of code that prints the total for all lines in numbers.txt
# or a file with any number of numbers.

number_file_read = open("numbers.txt", "r")
numbers = number_file_read.readlines()
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
print(f"result is: {sum(numbers)}")
number_file_read.close()

