def main():
    file_name = input("\nEnter the name of the file?)")
    write_file(file_name)
    sequential_read(file_name)
    seek_read(file_name)
    entire_read(file_name)


def write_file(file_name):
    input("\n________ In write_file() ________")

    input("\n Opening a file for WRITING only (an output file)")
    file_output1 = open(file_name, 'w')
    input(" > file_output1 = open(file_name, 'w'')")

    # tell() will tell the file position
    input("\n The tell() method finds out where the file pointer is")
    input(" Before first write, the file pointer position is : {}".format(file_output1.tell()))
    input(" > file_output1.tell()")

    input("\n Writing a line to the file")
    file_output1.write('An example of integer addition:\n')
    input(" > file_output1.write('An example of integer addition:\\n')")

    input("\n Current file pointer position is now : {}".format(file_output1.tell()))

    input("\n Writing a string 'integer' to the file")
    file_output1.write("5\n")
    input(" > file_output1.write('5\\n')")

    input("\n Current file pointer position is now : {}".format(file_output1.tell()))

    input("\n Writing another string 'integer' to the file")
    file_output1.write("10\n")
    input(" > file_output1.write('10\\n')")

    input("\n Current file pointer position is now : {}".format(file_output1.tell()))

    input("\n Closing the output file")
    input(" > file_output1.close()")
    file_output1.close()


def sequential_read(file_name):
    input("\n________ In read_file() ________")

    input("\n Opening a file for READING only (an input file)")
    file_input1 = open(file_name, 'r')
    input(" > file_input1 = open(file_name, 'r'')")

    input("\n Using the tell() method to report 1st file pointer position: {}".format(file_input1.tell()))

    input("\n Reading a line from the file:")
    input_string = file_input1.readline()
    input(" > input_string = file_input1.readline()")

    input("\n 2nd file pointer position: {}".format(file_input1.tell()))

    input("\n Reading a line from the file and converting the string to integer:")
    input_integer1 = int(file_input1.readline())
    input(" > input_integer1 = int(file_input1.readline())")

    input("\n 3rd file pointer position: {}".format(file_input1.tell()))

    input("\n Reading a line from the file and again converting the string to integer")
    input_integer2 = int(file_input1.readline())
    input(" > input_integer2 = int(file_input1.readline())")

    input("\n 4rd file pointer position: {}".format(file_input1.tell()))

    input("\n Adding two integers read from the file:")
    input(" > sum_of_ints = input_integer1 + input_integer2")
    sum_of_ints = input_integer1 + input_integer2

    input("\n Displaying read results")
    print("\n", input_string, input_integer2, '+',
          input_integer2, '=', sum_of_ints, sep='')
    input("")

    input("\n Closing the input file")
    input(" > file_input1.close()")
    file_input1.close()


# seek() will change the position
def seek_read(file_name):
    import fileinput
    input("\n________ In seek_read() ________")

    input("\n Opening a file for writing and reading (an i/o file)")
    file_seek1 = open(file_name, 'r+')
    input(" > file_seek1 = open(file_name, 'r+') ")

    input("Set file pointer to end of file")
    file_seek1.seek(0, 2)
    input(" > file_seek1.seek(0, 2)")

    input("\n Write a line to the file")
    file_seek1.write('This line was appended.\n')
    input(" > file_seek1.write('This line was appended.\\n')")

    input("\n Setting file pointer to byte position 36")
    file_seek1.seek(36)
    input(" > file_seek.seek(36)")

    input("\n Using the tell() method to report 1st file pointer position: {}".format(file_seek1.tell()))

    input("\n  Reading a line from the file and converting the string to integer:")
    input_integer2 = int(file_seek1.readline())
    input(" > input_integer2 = int(file_seek1.readline())")

    input("\n 2nd file pointer position: {}".format(file_seek1.tell()))

    input("\n Setting file pointer to byte position 33")
    file_seek1.seek(33)
    input(" > file_seek.seek(33)")

    input("\n  Reading a line from the file and again converting the string to integer:")
    input_integer1 = int(file_seek1.readline())
    input(" > input_integer1 = int(file_seek1.readline())")

    input("\n 3rd file pointer position: {}".format(file_seek1.tell()))

    input("\n Setting file pointer to byte position 0")
    file_seek1.seek(0)
    input(" > file_seek.seek(0)")

    input("\n Reading a line from the file")
    input_string = file_seek1.readline()
    input(" > input_string = file_seek1.readline()")

    input("\n Adding two integers read from the file")
    sum_of_ints = input_integer1 + input_integer2
    input(" > sum_of_ints = input_integer1 + input_integer2")

    input("\n Displaying read results")
    print("\n", input_string, input_integer2, '+',
          input_integer2, '=', sum_of_ints, sep='')
    input("")

    input("\n Closing the input file")
    input(" > file_seek1.close()")
    file_seek1.close()


def entire_read(file_name):
    input("\n________ In entire_read() ________")

    input("\n Opening a file for reading (an input file)")
    file_entire1 = open(file_name, 'r')
    input(" > file_entire1 = open(file_name, 'r')")

    input("\n Reading entire file into string entire_results")
    entire_results = file_entire1.read()
    input(" > entire_results = file_entire1.read()")

    input("\n Displaying read results")
    print(entire_results)
    input("")

    input("\n Closing the input file")
    input(" > file_entire1.close()")
    file_entire1.close()


if __name__ == '__main__':
    main()
else:
    pass
