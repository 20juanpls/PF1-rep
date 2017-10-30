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

# for each iteration of the loop, create a dictionary entry for the sales person data entered
# where the NAME is 'key' and the DEALERSHIP is the 'value'
while P_cont:
    print("  Please enter the sales person's:")
    sales_FN = input('    first name : ')
    sales_LN = input('    last name  : ')
    sales_deal = input('    dealership : ')
    print('  Requirement 4: entering name and dealership in dictionary ...')
    sales_name = (sales_FN+' '+sales_LN)
    sales_reps[sales_name] = sales_deal
    isStop = input('  Press Enter for another entry, type -1 to end entries: ')
    if isStop == '-1':
        P_cont = False
# |!| this is just a test string, comment later....
# print(str(sales_reps))

# you can just enter the information per person, and then per week, per day!!
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

# print(str(sales_data))

print('\nRequirement 8')
print("Type in the compliments given by the respective user for the following, "
      "If user has no further compliment's, press ENTER without typing")
print('\nRequirement 9')
complements_data = []
for person in sales_reps.keys():
    print('    '+person+"'s compliments:")
    FinalNumOfComp = 0
    Comp_c = True
    count = 0
    while Comp_c:
        Comp_int = input('   '+str(count+1)+'. ')
        if Comp_int == '':
            FinalNumOfComp = count
            Comp_c = False
        count += 1
    complements_data.append(FinalNumOfComp)
# print(str(complements_data))

print('\nRequirement 10')
PersonCount = 0
for person, dealership in sales_reps.items():
    print('--------------------------------------')
    print(person+' of '+dealership)
    print('Cars Sold')
    totalCars = 0
    WeekCount = 0
    for week in weeks:
        print('\n'+week)
        DayCount = 0
        for day in days:
            CarsSold = sales_data[WeekCount][DayCount][PersonCount]
            print(day+': ' + str(CarsSold))
            totalCars += CarsSold
            DayCount += 1
        WeekCount += 1
    print("\nTotal Cars Sold (per rep): " + str(totalCars))
    print("Average Cars Sold (per rep): " + str(round(totalCars / 6)))
    print("Number of Compliments (per rep): " + str(complements_data[PersonCount]))
    PersonCount += 1






