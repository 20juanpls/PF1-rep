# main() function < the one that rules it all!...
def main():
    print('\nThis is Program 6')
    # function req1
    requirement_1()
    # using a function to create the 2 tuples
    weeks, days = requirement_2()
    print('created tuples:')
    print("     weeks = " + str(weeks))
    print("     days = " + str(days))

    print('\nRequirement 3')
    print('Please record the names of the sales people, and the name of the dealership they work in:')
    p_cont = True
    sales_reps = {}
    # for each iteration of the loop, create a dictionary entry for the sales person data entered
    # where the NAME is 'key' and the DEALERSHIP is the 'value'
    while p_cont:
        # user inputs variables in requirement_3()
        first_name, last_name, dealership = requirement_3()
        # populates dictionary sales_reps in requirement_4()
        requirement_4(sales_reps, first_name, last_name, dealership)
        # asks to user if they are finished putting entries
        is_stop = input('  Press Enter for another entry, type -1 to end entries: ')
        if is_stop == '-1':
            p_cont = False
    # |!| this is just a test string, comment later....
    print(str(sales_reps))


def requirement_1():
    print('\nRequirement 1')
    print('This program practices working with lists, strings, tuples, and dictionaries.')


# Creating and returning the week and day tuples
def requirement_2():
    print('\nRequirement 2')
    weeks_tuple = ('Week One', 'Week Two')
    days_tuple = ('Thursday', 'Friday', 'Saturday')
    return weeks_tuple, days_tuple


# user enters the first name, last name, and the dealership of a sales person
def requirement_3():
    print("  Please enter the sales person's:")
    sales_fn = input('    first name : ')
    sales_ln = input('    last name  : ')
    sales_deal = input('    dealership : ')
    return sales_fn, sales_ln, sales_deal


# enters the full name and the dealership of the dealer in the dictionary
def requirement_4(representatives, fn, ln, deal):
    print('  Requirement 4: entering name and dealership in dictionary ...')
    sales_name = (fn + ' ' + ln)
    representatives[sales_name] = deal


# 11/6/17 - I am allowed to call req 6 and 7 from a the req5 function,
# that means im nor restricted to calling all of the req functions from main.
def requirement_5():
    print()


# This determines if program is main or module
if __name__ == '__main__':
    main()
else:
    pass
# do nothing. By passing it allows other programs to import from
# this module :)
