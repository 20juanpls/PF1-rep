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
    print('  Input values for:')
    x = int(input('x = '))
    y = int(input('y = '))
    two = 2
    three = 3

    p_num = x + y
    input('Addition:               x + y = ' + str(p_num))
    p_num = x - y
    input('Subtraction:            x - y = ' + str(p_num))
    p_num = x * 5
    input('Multiplication:         x * 5 = ' + str(p_num))
    p_num = x / two
    input('Division:             x / two = ' + str(p_num))
    p_num = x // two
    input('Integer Division:    x // two = ' + str(p_num))
    p_num = x % three
    input('Modulo (remainder): x % three = ' + str(p_num))
    p_num = x ** two
    input('Exponentiation:      x ** two = ' + str(p_num) + '\n')

    p_bool = (x > y)
    input('x > y = ' + str(p_bool))
    p_bool = (x < y)
    input('x < y = ' + str(p_bool))
    p_bool = (x >= 5)
    input('x >= 5 = ' + str(p_bool))
    p_bool = (x <= 2)
    input('x <= two = ' + str(p_bool))
    p_bool = (x == y)
    input('x == y = ' + str(p_bool))
    p_bool = (x != three)
    input('x != three = ' + str(p_bool) + '\n')

    p_bool = (x > y and x >= 33)
    input('x > y and x >= 33: ' + str(p_bool))
    p_bool = (x < y or x <= 33)
    input('x < y or x <= 33:  ' + str(p_bool))
    p_bool = not(x <= 33)
    input('not (x <= 33):     ' + str(p_bool) + '\n')

    a = 5
    input('a = '+str(a))
    id_hex = hex(id(a))
    input('a points to: '+id_hex)

    b = 5
    input('b = '+str(b))
    id_hex = hex(id(b))
    input('b points to: '+id_hex)
    p_bool = (a == b)
    input('a == b : '+str(p_bool))
    p_bool = (a is b)
    input('a is b : '+str(p_bool))

    c = 5.0
    input('\nc = '+str(c))
    id_hex = hex(id(c))
    input('c points to: '+id_hex)
    p_bool = (a == c)
    input('a == c : '+str(p_bool))
    p_bool = (a is c)
    input('a is c : '+str(p_bool))
    input("converting 'a' into a float: a = " + str(float(a)))
    input("converting 'c' into an integer: c = "+str(int(c)))

    a = '\nPython is fun.'
    input(a)
    a = 5
    input('\na = '+str(a)+"; 'a' is now an integer.")
    b = str(b)
    input('b = '+b+"; 'b' is now a string.")
    p_bool = (a == b)
    input('a == b : '+str(p_bool))
    id_hex = hex(id(a))
    input('a points to: '+id_hex)
    id_hex = hex(id(b))
    input('b points to: '+id_hex)

    num = sys.maxsize
    input('\nVariable maxsize = '+str(num))
    input('Variable minsize = '+str(num*-1))

    import math
    input('Math has been imported!!!')

    input('\nPositive infinity = '+str(math.inf))
    input('Negative infinity = '+str(-math.inf))

    input("\nConverting infinity into a float... using variable 'test'")
    test = float("inf")
    input('Positive infinity = ' + str(test))
    input('Negative infinity = ' + str(-test))

    input('\nTesting for positive or negative infinity')
    input('Is test infinity = ' + str(math.isinf(test)))
    input('Is -test infinity = ' + str(math.isinf(-test)))

    input('\nNan examples')
    a = math.nan
    input('math.nan :' + str(a))
    input('a = ' + str(a))


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
