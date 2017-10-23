from time import sleep
import sys
# Just a test review


def main():
    not_done = True
    while not_done:
        print('\n--------------------Unit 2 Review - Data Types--------------------')
        print('Please input the number cooresponding the Data Type topic:')
        print('1. Data Types - Numbers')
        print('2. Data Types - Sequences')
        print('3. Data Types - Mapping')
        print('4. Data Types - Sets')
        print('Ltrly anything else 4 exiting')
        select_num = input('')

        if select_num == '1':
            not_done = dt_numbers()
        elif select_num == '2':
            not_done = dt_sequences()
        elif select_num == '3':
            not_done = dt_mapping()
        elif select_num == '4':
            not_done = dt_sets()
        else:
            print('but y tho ... :(')
            not_done = False


def dt_numbers():
    print('--------------------Data Types - Numbers--------------------')
    print("Numbers come in integrals('int' & 'boolean'), real ('floating'), and complex")
    input('')
    print(" Mathematical Operations - Examples")
    input('')
    print('  Input values for:')
    x = int(input('  x = '))
    y = int(input('  y = '))
    two = 2
    three = 3

    p_num = x + y
    input('  Addition:               x + y = ' + str(p_num))
    p_num = x - y
    input('  Subtraction:            x - y = ' + str(p_num))
    p_num = x * 5
    input('  Multiplication:         x * 5 = ' + str(p_num))
    p_num = x / two
    input('  Division:             x / two = ' + str(p_num))
    p_num = x // two
    input('  Integer Division:    x // two = ' + str(p_num))
    p_num = x % three
    input('  Modulo (remainder): x % three = ' + str(p_num))
    p_num = x ** two
    input('  Exponentiation:      x ** two = ' + str(p_num) + '\n')

    p_bool = (x > y)
    input('  x > y = ' + str(p_bool))
    p_bool = (x < y)
    input('  x < y = ' + str(p_bool))
    p_bool = (x >= 5)
    input('  x >= 5 = ' + str(p_bool))
    p_bool = (x <= 2)
    input('  x <= two = ' + str(p_bool))
    p_bool = (x == y)
    input('  x == y = ' + str(p_bool))
    p_bool = (x != three)
    input('  x != three = ' + str(p_bool) + '\n')

    p_bool = (x > y and x >= 33)
    input('  x > y and x >= 33: ' + str(p_bool))
    p_bool = (x < y or x <= 33)
    input('  x < y or x <= 33:  ' + str(p_bool))
    p_bool = not(x <= 33)
    input('  not (x <= 33):     ' + str(p_bool) + '\n')

    a = 5
    input('  a = '+str(a))
    id_hex = hex(id(a))
    input('  a points to: '+id_hex)

    b = 5
    input('  b = '+str(b))
    id_hex = hex(id(b))
    input('  b points to: '+id_hex)
    p_bool = (a == b)
    input('  a == b : '+str(p_bool))
    p_bool = (a is b)
    input('  a is b : '+str(p_bool))

    c = 5.0
    input('\n  c = '+str(c))
    id_hex = hex(id(c))
    input('  c points to: '+id_hex)
    p_bool = (a == c)
    input('  a == c : '+str(p_bool))
    p_bool = (a is c)
    input('  a is c : '+str(p_bool))
    input("  converting 'a' into a float: a = " + str(float(a)))
    input("  converting 'c' into an integer: c = "+str(int(c)))

    a = '\n   Python is fun.'
    input(a)
    a = 5
    input('\n  a = '+str(a)+"; 'a' is now an integer.")
    b = str(b)
    input('  b = '+b+"; 'b' is now a string.")
    p_bool = (a == b)
    input('  a == b : '+str(p_bool))
    id_hex = hex(id(a))
    input('  a points to: '+id_hex)
    id_hex = hex(id(b))
    input('  b points to: '+id_hex)

    num = sys.maxsize
    input('\n  Variable maxsize = '+str(num))
    input('  Variable minsize = '+str(num*-1))

    import math
    input('  Math has been imported!!!')

    input('\n  Positive infinity = '+str(math.inf))
    input('  Negative infinity = '+str(-math.inf))

    input("\n  Converting infinity into a float... using variable 'test'")
    test = float("inf")
    input('  Positive infinity = ' + str(test))
    input('  Negative infinity = ' + str(-test))

    input('\n  Testing for positive or negative infinity')
    input('  Is test infinity = ' + str(math.isinf(test)))
    input('  Is -test infinity = ' + str(math.isinf(-test)))

    input('\n  Nan examples')
    a = math.nan
    input('  math.nan :' + str(a))
    input('  a = ' + str(a))

    is_it_done = the_question('Numbers')
    return is_it_done


def dt_sequences():
    print('--------------------Data Types - Sequences--------------------')
    input('<<<<<<Immutable Sequences - Tuples>>>>>>')
    input(' There are two tuples created...')
    tuple1 = ('apple', 'pear', 'cherry')
    tuple2 = ('pup', 'kitty', 'cub')
    input('  tuple1 = '+str(tuple1)+'\n  tuple2 = '+str(tuple2))
    fruit = 'pear'
    input("  and now: fruit = 'pear'")

    input('\n  fruit in tuple1: '+str(fruit in tuple1))
    input('\n  fruit not in tuple1:'+str(fruit not in tuple1))
    input('\n  Adding tuple1 and tuple2 <tuple1 + tuple2>:')
    input('  '+str(tuple1+tuple2))
    input('\n  Duplicating tuple1 n number of times <tuple1 * 2>:')
    input('  '+str(tuple1*2))
    input('\n  Returning item in with index 2 in tuple2 <tuple2[2]>:')
    input('  '+tuple2[2])
    input('\n  Conecatenate the two tuples to create tuple3 <tuple3 = tuple1 + tuple2>:')
    tuple3 = tuple1 + tuple2
    input('  '+str(tuple3))
    input('\n  Slice tuple3 from indexes 2 to 5 (non-inclusive)<tuple3[2:5]>:')
    input('  '+str(tuple3[2:5]))
    input('\n  Slice tuple3 from indexes 1 to 5 with step 2 <tuple3[1:5:2]>:')
    input('  '+str(tuple3[1:5:2]))
    input('\n  Length of tuple3 <len(tuple3)>:')
    input('  '+str(len(tuple3)))
    input('\n  Smallest item in tuple3 <min(tuple3)>:')
    input('  '+min(tuple3))
    input('\n  Largest item in tuple3 <max(tuple3)>:')
    input('  '+max(tuple3))
    input('\n  PAY ATTENTION TO THE ONE WITH THE LARGEST AND SMALLEST HEX-DECIMAL VALUE!!!!!')
    for x in range(0, len(tuple3)):
        if tuple3[x] == min(tuple3):
            print("   " + hex(id(tuple3[x])) + " : " + tuple3[x] + " <-- SMALLEST VALUE")
        elif tuple3[x] == max(tuple3):
            print("   " + hex(id(tuple3[x])) + " : " + tuple3[x] + " <-- LARGEST VALUE")
        else:
            print("   " + hex(id(tuple3[x]))+" : "+tuple3[x])

    input('\n  Returning the index of where pup was found <tuple3.index("pup", 2, 5)>:')
    input('  '+str(tuple3.index("pup", 2, 5)))
    input('\n  How many "cub" in tuple3? <tuple3.count("cub")>:')
    input('  '+str(tuple3.count("cub")))

    input('\n<<<<<<Mutable Sequences - Lists>>>>>>')

    is_it_done = the_question('Sequences')
    return is_it_done


def dt_mapping():
    print('--------------------Data Types - Mapping--------------------')
    is_it_done = the_question('Mapping')
    return is_it_done


def dt_sets():
    print('--------------------Data Types - Sets--------------------')
    is_it_done = the_question('Sets')
    return is_it_done


def the_question(review_type):
    print('Data Type - '+review_type+' review finished!')
    the_answer = input('Would you like to select another Data type review?( y or n ): ')
    if the_answer == 'y':
        return True
    else:
        return False


if __name__ == '__main__':
    main()

else:
    pass
