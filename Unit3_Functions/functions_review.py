# import functions_1
# import functions_0
import os


def main():
    print("[[[[[[[[[[[[[[[[[[[[[[[[[[functions_review]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
    program_menu = True
    directory = directory_search()
    while program_menu:
        print("\nInput the number cooresponding to the program you want to run:")
        print("1) functions_0.py")
        print("2) functions_1.py")
        print("3) EXIT")
        user_in = input("")

        if user_in == '1':
            os.system('python'+directory+'/functions_0.py')
            # exec(open("functions_0.py").read())
            done_question()
        elif user_in == '2':
            os.system('python'+directory+'/functions_1.py')
            # exec(open("functions_1.py").read())
            done_question()
        elif user_in == '3':
            print("Bye! :)")
            return False
        else:
            print("I'm sorry, but that is not a valid answer...")


def directory_search():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    dir_list = current_dir.split('\\')
    new_dir_list = []
    for x in range(1, len(dir_list)):
        temp = '/'+dir_list[x]
        new_dir_list.append(temp)
    new_dir = ''.join(new_dir_list)
    return new_dir


def done_question():
    print("___________________PROGRAM_FINISHED_________________________________")


if __name__ == '__main__':
    main()

else:
    pass
