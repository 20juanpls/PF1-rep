# main() function < the one that rules it all!...
def main():
    print('\nThis is Program 7')
    # function req1
    requirement_1_intro()
    # using a function to create the 2 tuples
    weeks, days = create_tuples()
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
        # user inputs variables in sales_person_info; Req 3
        first_name, last_name, dealership = sales_person_info()
        # populates dictionary sales_reps in set_dealership_dictionary(...); Req 4
        set_dealership_dictionary(sales_reps, first_name, last_name, dealership)
        # asks to user if they are finished putting entries
        is_stop = input('  Press Enter for another entry, type -1 to end entries: ')
        if is_stop == '-1':
            p_cont = False
    # |!| this is just a test string, comment later....
    # print(str(sales_reps))

    print('\nRequirement 5, 6 & 7')
    print('processing sales data...')
    # Req 5, 6 & 7 - user inputs the sales data per person, per day, per week
    sales_data = week_days_loop_setup(weeks, days, sales_reps)

    # Req 8 & 9 - user enters the compliments of each person, while the function(s) will couunt
    # how many compliments did a sales person make
    complements_data = populating_complements(sales_reps)

    # Req 10 - prints the final receipt/sales data per person and dealer
    print_receipt(sales_reps, sales_data, complements_data, weeks, days)

    # Req 11
    program_7_statement()


# Requirement 1, the intro
def requirement_1_intro():
    print('\nRequirement 1')
    print('This program practices working with lists, strings, tuples, and dictionaries.')


# Requirement 2
# Creating and returning the week and day tuples
def create_tuples():
    print('\nRequirement 2')
    weeks_tuple = ('Week One', 'Week Two')
    days_tuple = ('Thursday', 'Friday', 'Saturday')
    return weeks_tuple, days_tuple


# Requirement 3
# user enters the first name, last name, and the dealership of a sales person
def sales_person_info():
    print("  Please enter the sales person's:")
    sales_fn = input('    first name : ')
    sales_ln = input('    last name  : ')
    sales_deal = input('    dealership : ')
    return sales_fn, sales_ln, sales_deal


# Requirement 4
# stores the full name and the dealership of the dealer in the dictionary
def set_dealership_dictionary(representatives, fn, ln, deal):
    print('  Requirement 4: entering name and dealership in dictionary ...')
    sales_name = (fn + ' ' + ln)
    representatives[sales_name] = deal


# Requirement 5
# 11/6/17 - I am allowed to call req 6 and 7 from a the req5 function,
# that means im nor restricted to calling all of the req functions from main.
# function <requirement 5> returns a sales_data list.
def week_days_loop_setup(weeks, days, sales_reps):
    sales_data = []
    for week in weeks:
        weekly_records = []
        print('---------- Entering cars for ' + week + ' ----------')
        days_loop(weekly_records, days, sales_reps)
        sales_data.append(weekly_records)
    return sales_data


# Requirement 6
# days tuple loop function; called by requirement_5
def days_loop(weekly_records, days, sales_reps):
    for day in days:
        daily_records = []
        print('  '+day+':')
        sales_reps_loop(daily_records, sales_reps)
        weekly_records.append(daily_records)


# Requirement 7
# sales data loop function; called by requirement_6
def sales_reps_loop(daily_records, sales_reps):
    for person in sales_reps.keys():
        num_of_cars = int(input('   Number of cars sold by ' + person + ': '))
        daily_records.append(num_of_cars)


# Requirement 8
# creates loop to populate a list of customer compliments
def populating_complements(sales_reps):
    print('\nRequirement 8 & 9')
    print("Type in the compliments given by the respective user for the following,"
          "\nIf user has no further compliments, Type '-1' or press ENTER without typing")
    complements = []
    for person in sales_reps.keys():
        print(' ' + person + "'s compliments:")
        final_num_of_comp = 0
        comp_c = True
        count = 0
        continue_complementing(complements, final_num_of_comp, comp_c, count)
    return complements


# Requirement 9
# for every complement, it reads whether the user wants to continue to enter
# or stop entering. it also appends a number of compliments to the list
# compliments; called by requirement_8
def continue_complementing(complements, final_num, c_c, count):
    while c_c:
        comp_int = input('   ' + str(count + 1) + '. ')
        if comp_int == '' or comp_int == '-1':
            final_num = count
            c_c = False
        count += 1
    complements.append(final_num)


#  Requirement 10
# Prints the final receipt per person
def print_receipt(sales_reps, sales_data, complements_data, weeks, days):
    for person, dealership in sales_reps.items():
        print('--------------------------------------')
        print(person + ' of ' + dealership)
        print('Cars Sold')
        total_cars = 0
        for week in weeks:
            print('\n' + week)
            for day in days:
                cars_sold = sales_data[weeks.index(week)][days.index(day)][list(sales_reps.keys()).index(person)]
                print(day + ': ' + str(cars_sold))
                total_cars += cars_sold
        print("\nTotal Cars Sold: " + str(total_cars))
        print("Average Cars Sold: " + str(round(total_cars / 6)))
        print("Number of Compliments: " + str(complements_data[list(sales_reps.keys()).index(person)]))


# Requirement 11
# A statement regarding Program 7
def program_7_statement():
    print("\nI liked program_7. It refreshed my memory of how functions, and using their parameters"
          "\nand arguments, work. I look forward to making complex programs using modules real"
          "\nsoon.")


#  This determines if program is main or module
if __name__ == '__main__':
    main()
else:
    pass
# do nothing. By passing it allows other programs to import from
# this module :)
