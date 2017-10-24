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
    input("\n  and now: fruit = 'pear'")

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
    input(' there are four list created...')
    list1 = ['Computer Science', 'English', 'Physiology']
    list2 = ['Papua New Guinea', 'Argentina', 'America']
    list3 = [1, 3, 5, 7, 9]
    list4 = ['Wonderful', 'Life', 'True dat']
    input('  list1 = ' + str(list1) + '\n  list2 = ' + str(list2) + '\n  list3 = ' + str(list3) +
          '\n  list4 = ' + str(list4))
    list1[2] = 'Humanities'
    input("\n  Replacing list[2] from 'Physiology' to 'Humanities' <list1[2] = 'Humanities'>")
    input('  list1 = '+str(list1))
    list3[2:1] = list2
    input("\n  Replace list3[2:1] to list2 <list3[2:1] = list2>")
    input('  list3 = '+str(list3))
    list3 = [1, 3, 5, 7, 9]
    input('\n  Resetting list3')
    input('  list3 = '+str(list3))
    list3[2] = list2
    input('\n  Inserting list2 within list3 <list3[2] = list2>')
    input('  list3 = '+str(list3))
    del list3[1:4]
    input('\n  Deleting indexes 1 - 4 (non-inclusive)<del list3[1:4]>')
    input('  list3 = '+str(list3))
    list3 = [1, 3, 5, 7, 9]
    input('\n  Resetting list3 again')
    input('  list3 = ' + str(list3))
    list3[1:3:1] = list4
    input('\n  s[i:j:k] = t')
    input('  t must have the same length as the slice its replacing, and k is the step value')
    input('  list3[1:3:1] = list4')
    input('  list3 = '+str(list3))
    del list3[0:5:2]
    input('\n  del s[i:j:k]')
    input('  Deleting 0 - 5 step 2 <del list3[0:5:2]>')
    input('  list3 = '+str(list3))
    list3.append('All the Best')
    input("\n  Appending 'All the Best' in list3 <list3.append('All the Best')>")
    input('  list3 = '+str(list3))
    list3.clear()
    input("\n  Clearing list3 <list3.clear()>")
    input('  list3 = '+str(list3))
    list3 = [1, 3, 5, 7, 9]
    input('\n  Resetting list3 yet again')
    input('  list3 = ' + str(list3))
    list4.extend(list3)
    input('\n  Extending contents of list4 with contents of list3 <list4.extend(list3)>')
    input('  list4 = '+str(list4))
    list3 *= 2
    input('\n  Multiplying list3 contents times 2 <list3 *= 2>')
    input('  list3 = '+str(list3))
    list3.insert(4, 'Hey There')
    input("\n  Inserting 'Hey There' in list3[4] <list3.insert(4,'Hey There')>")
    input('  list3 = '+str(list3))
    item_removed = list4.pop(2)
    input('\n  Popping item in list4[2] out of list4 <item_removed = list4.pop(2)>')
    input('  list4 = '+str(list4)+'\n  item_removed = '+item_removed)
    list4.remove(5)
    input('\n  Removing item in list4[5] <list4.remove(5)>')
    input('  list4 = '+str(list4))
    input('  NOTICE HOW IT REMOVES list4[5] FROM WHEN THE list4 WAS ON THE STATE BEFORE THE POP'
          "\n  before pop : ['Wonderful', 'Life', 'True dat', 1, 3, 5<to be removed>, 7, 9]"
          "\n  after pop  :   ['Wonderful', 'Life', <'True dat' popped>, 1, 3, 5<to be removed>, 7, 9]")
    list4.reverse()
    input('\n  Reversing list4 <list4.reverse()>')
    input('  list4 = '+str(list4))
    print('')
    is_it_done = the_question('Sequences')
    return is_it_done


def dt_mapping():
    print('--------------------Data Types - Mapping--------------------')
    print(' Creating an empty dictionary...')
    home_state = {}
    print(type(home_state))
    home_state = {'Miesha': 'Florida', 'Rodger': 'Nebraska', 'Sheldon': 'Arizona',
                  'Merissa': 'Hawaii', 'William': 'Washington', 'Clora': 'California'}
    input("  home_state = {'Miesha': 'Florida', 'Rodger': 'Nebraska', 'Sheldon': 'Arizona',"
          "\n                'Merissa': 'Hawaii', 'William': 'Washington', 'Clora': 'California'}")
    input('\n  dictionary.values()')
    input('  Returning values as a sequence of tuples <home_state.values()>')
    input('  '+str(home_state.values()))
    input('\n  dictionary.pop() returns the value AND removes the item'
          "\n  'Sheldon not found - pop' is the 'default' and will be shown"
          "\n  if the item is not found in the dictionary")
    value = home_state.pop('Sheldon', 'Sheldon not found - pop')
    input("  <value = home_state.pop('Sheldon', 'Sheldon not found - pop')>")
    input("  value = '"+str(value) + "' from Sheldon pop.")
    input("  the Key is 'Sheldon', the value is 'Arizona' !!!")
    input('\n  dictionary.get() returns the value but does not remove')
    value = home_state.get('Rodger', 'Rodger Not found - get')
    input("  <value = home_state.get('Rodger', 'Rodger Not found - get')>")
    input("  value = '" + str(value) + "' from Rodger get.")
    input("  the Key is 'Rodger', the value is 'Nebraska' !!!")
    input('\n  And now lets go check at the values with dictionary.values() <home_state.values()>')
    input('  '+str(home_state.values()))
    input('\n  Confirming if item exist before deleting with IF statement, otherwise get KeyError exception')
    if 'William' in home_state:
        del home_state['William']
        input("  item 'William' deleted.")
    else:
        input("  'William' is not in the dictionary")
    input("\n  If William was deleted, then that means 'William': 'Washington' was deleted")
    input('  home_state = '+str(home_state))
    input("\n  Confirming if item exists before accessing with IF statement, otherwise ger KeyError exception")
    if 'George' in home_state:
        value = home_state['George']
        input("  value = '"+str(value)+"' associated with key 'George'")
    else:
        input("  'George' is not in the dictionary")
    input('\n  dictionary.get() returns the value but does not remove')
    input("  <value = home_state.get('William', 'William not found -')>")
    value = home_state.get('William', 'William not found -')
    input("  '"+str(value)+"' from 'William' get.")
    input('\n  dictionary.clear() removes all items <home_state.clear>')
    home_state.clear()
    input('  home_state cleared: home_state = '+str(home_state))
    input("\n  Adding a new item to the dictionary <home_state['Joe'] = 'Louisiana'>")
    home_state['Joe'] = 'Louisiana'
    input('  Now printing all the values in home_state using For loop:')
    for value in home_state.values():
        print("   "+value)
    input("")
    input("  Adding another item to the dictionary <home_state['Abe'] = 'Montana'>")
    home_state['Abe'] = 'Montana'
    input('  Now printing all the values in home_state using For loop:')
    for value in home_state.values():
        print("   "+value)
    input("")
    input("  Now adding yet another item to the dictionary <home_state['Bert'] = 'Tennessee'>")
    home_state['Bert'] = 'Tennessee'
    input("  Now printing the items using dictionary.items() in a For loop, which will return all"
          "\n  keys and values")
    input(">  for key, value in home_state.items():"
          "\n>      print(key, value)")
    for key, value in home_state.items():
        print("   ", key, value)
    input("")
    input("  Now printing the keys using dictionary.keys() in a For loop, which will return all keys")
    input(">  for key in home_state.keys():"
          "\n>      print(key)")
    for key in home_state.keys():
        print("   "+key)
    input("")
    input("  dictionary.popitem() will return a randomly selected variable"
          "\n  AND removes that item")
    input(">  value = home_state.popitem()")
    value = home_state.popitem()
    input("  '"+str(value)+"' was popitemed!")
    input("\n  Now we check if 'Abe' key is in the dictionary using an If statement")
    if 'Abe' in home_state:
        input("  I found 'Abe' key")
    else:
        input("  'Abe' key must have been popitemed.")
    input("\n  Now checking if 'George' key is NOT in the dictionary using an If statement")
    if 'George' not in home_state:
        input("  I did not find key 'George'")
    input('  Now we will loop through dictionary.items() and it will return all keys and values')
    for key, value in home_state.items():
        print("   ", key, value)
    input('')
    input("  Find the key for a specified value; First determine if value is in the dictionary")
    input("  In this case the value is 'Tennessee', and we would be looking for its key and value"
          "\n  using a For loop")
    input(">  for key, value in home_state.items():"
          "\n>      if value == 'Tennessee':"
          "\n>          found = True    <we have found the value>"
          "\n>          found_key = key <now we set found_key to key>")
    found = False
    found_key = None
    for key, value in home_state.items():
        if value == 'Tennessee':
            found = True
            found_key = key
    if found:
        input("  Key '"+found_key+"' was found.")
    else:
        input("  value 'Tennessee' was not found in dictionary.")
    input("Our final dictionary is:"
          "home_state = "+str(home_state))
    is_it_done = the_question('Mapping')
    return is_it_done


def dt_sets():
    print('--------------------Data Types - Sets--------------------')
    is_it_done = the_question('Sets')
    return is_it_done


def the_question(review_type):
    print('\nData Type - '+review_type+' review finished!')
    the_answer = input('Would you like to select another Data type review?( y or n ): ')
    if the_answer == 'y':
        return True
    else:
        return False


if __name__ == '__main__':
    main()

else:
    pass
