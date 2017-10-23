from time import sleep
import sys
# Just a test review

def main():
    print('Please input the number cooresponding the Data Type topic:')
    print('1. Data Types - Numbers')
    print('2. Data Types - Sequences')
    print('3. Data Types - Mapping')
    print('4. Data Types - Sets')
    select_num = input('')

    if select_num == '1':
        dt_numbers()
    elif select_num == '2':
        dt_sequences()
    elif select_num == '3':
        dt_mapping()
    elif select_num == '4':
        dt_sets()
    else:
        print('but y tho ... :(')


def dt_numbers():
    print('--------------------Data Types - Numbers--------------------')
    print("Numbers come in integrals('int' & 'boolean'), real ('floating'), and complex")
    input('')
    print(" Mathematical Operations - Examples")
    input('')
    x = 77


def dt_sequences():
    print('--------------------Data Types - Sequences--------------------')


def dt_mapping():
    print('--------------------Data Types - Mapping--------------------')


def dt_sets():
    print('--------------------Data Types - Sets--------------------')


if __name__ == '__main__':
    main()

else:
    pass
