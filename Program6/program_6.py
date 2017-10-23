print('\nThis is Program 6')
print('\nRequirement 1')
print('This program practices working with lists, strings, tuples, and dictionaries.')

print('\nRequirement 2')
weeks = ('Week One', 'Week Two')
days = ('Thursday', 'Friday', 'Saturday')
# Displays the tuples
print('created tuples:')
print("     weeks = "+str(weeks))
print("     days = "+str(days))

# Enter the first and last names of the sales people, and the name of the dealership they work for...
print('\nRequirement 3')
print('Please record the names of the sales people, and the name of the dealership they work in:')
sales_reps = {}
P_cont = True
while P_cont:
    sales_FN = input('  Please enter the sales person first name: ')
    sales_LN = input('  Please enter the sales person last name: ')
    sales_deal = input('  Please enter the dealership the sales person work in: ')
    print('  Requirement 4: entering name and dealership in dictionary ...')
    sales_name = (sales_FN+' '+sales_LN)
    sales_reps[sales_name] = sales_deal
    print('  Press Enter for another entry, type -1 to end entries')
    isStop = input('    ')
    if isStop == '-1':
        P_cont = False
# |!| this is just a test string, comment later....
# print(str(sales_reps))

print('\nRequirement 5')
print('processing sales data...')
sales_data = []
for week in weeks:
    weekly_records = []
    print('---------- Entering cars for '+week+' ----------')
    for day in days:
        daily_records = []
        print('  '+day+':')
        for person in sales_reps.keys():
            num_of_cars = int(input('   Number of cars sold by '+person+': '))
            daily_records.append(num_of_cars)
        weekly_records.append(daily_records)
    sales_data.append(weekly_records)

print(str(sales_data))






