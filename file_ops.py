file_name = "test.txt"
lines = ["Line 1", "Line 2", "Line 3", "Line 4"]

# write to a file
with open(file_name, 'w') as writer:
    # write lines from list
    writer.writelines(line + '\n' for line in lines)

# open and read from a file
with open(file_name, 'r') as reader:
    # Read & print the entire file
    print(reader.read())

# Read and print the entire file line by line
with open(file_name, 'r') as reader:
    for line in reader:
        print(line, end='')
