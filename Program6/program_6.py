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
print('\nRequirement 5, 6 & 7')
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
print("Type in the compliments given by the respective user for the following,"
      "\nIf user has no further compliments, Type '-1' or press ENTER without typing")
print('\nRequirement 9')
complements_data = []
for person in sales_reps.keys():
    print(' '+person+"'s compliments:")
    FinalNumOfComp = 0
    Comp_c = True
    count = 0
    while Comp_c:
        Comp_int = input('   '+str(count+1)+'. ')
        if Comp_int == '' or Comp_int == '-1':
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
    print("\nTotal Cars Sold: " + str(totalCars))
    print("Average Cars Sold: " + str(round(totalCars / 6)))
    print("Number of Compliments: " + str(complements_data[PersonCount]))
    PersonCount += 1

print("\nRequirement 11")
print("This program was kind of weird for me at first because I didn't quite understood"
      "\nwhat exactly was it asking from me in requirements 5 - 7. I decided to work on"
      "\nwhat the instructions required me to do, which required the user to input the "
      "\nnumber of cars sold per day, per week; which meant that I had to loop through "
      "\nthe 2 weeks, than days, than through everyone in the dictionary. It was only a"
      "\ncouple of days ago where I found out that you(the instructor) were lenient of"
      "\nwhat ever method the student decided to approach those requirement; and though"
      "\nI could change it ... I've already went through the effort of making the loops"
      "\nsequence that way. Besides, I believe the user will have an easier time placing"
      "\nin the data by per Dealer per Day. Overall, I thought is was a fun, though"
      "\nat first confusing, assignment")




