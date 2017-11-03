import os

path = os.path.dirname(os.path.realpath(__file__))

budget_data1 = "budget_data_1.csv"

import csv
with open(budget_data1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    count = 0
    Total = 0
    budget = {'Date':[],
                'Revenue': []}
    # Create dictionary with keys 'Date' and 'Revenue' and lists of their respective values
    for row in csvreader:
        budget['Date'].append(row[0])
        budget['Revenue'].append(row[1])

    # Remove string 'Date' and 'Revenue' from list so you get only date and revenue in dict
    budget['Date'].remove('Date')
    budget['Revenue'].remove('Revenue')

    Date = budget['Date']
    Revenue = list(map(int, budget['Revenue']))

    # Begin output of Financial Analysis
    print("Financial Analysis")
    print("----------------------------")

    for month in Date:
        count += 1
    print('Total Months: ' + str(count))

    for rev in Revenue:
        Total += int(rev)
    print('Total Revenue: $' + str(Total))

    Max_Rev = max(Revenue)
    print('Greatest Increase in Revenue: ' + budget['Date'][Revenue.index(Max_Rev)] + ' ($'+str(Max_Rev)+')')

    Min_Rev = min(Revenue)
    print('Greatest Decrease in Revenue: ' + budget['Date'][Revenue.index(Min_Rev)] + ' ($'+str(Min_Rev)+')')
    print()

# Textfile output
filename = 'Financial Analysis Budget Data 1_MG.txt'
with open(filename, 'w') as textfile:
    # 
    textfile.write('Financial Analysis\n')
    textfile.write('----------------------------\n')
    textfile.write('Total Month: ' + str(count) + '\n')
    textfile.write('Total Revenue: $' + str(Total) + '\n')
    textfile.write('Greatest Increase in Revenue: ' + budget['Date'][Revenue.index(Max_Rev)] + ' ($'+str(Max_Rev)+')' + '\n')
    textfile.write('Greatest Decrease in Revenue: ' + budget['Date'][Revenue.index(Min_Rev)] + ' ($'+str(Min_Rev)+')')

# -----------------------------------------------------------------------------------------------------------

# Financial Analysis for budget_data_2

budget_data2 = "budget_data_2.csv"

with open(budget_data2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    count = 0
    Total = 0
    budget = {'Date':[],
                'Revenue': []}
    # Create dictionary with keys 'Date' and 'Revenue' and lists of their respective values
    for row in csvreader:
        budget['Date'].append(row[0])
        budget['Revenue'].append(row[1])

    # Remove string 'Date' and 'Revenue' from list so you get only date and revenue in dict
    budget['Date'].remove('Date')
    budget['Revenue'].remove('Revenue')

    Date = budget['Date']
    Revenue = list(map(int, budget['Revenue']))

    # Begin output of Financial Analysis
    print("Financial Analysis")
    print("----------------------------")

    for month in Date:
        count += 1
    print('Total Months: ' + str(count))

    for rev in Revenue:
        Total += int(rev)
    print('Total Revenue: $' + str(Total))

    Max_Rev = max(Revenue)
    print('Greatest Increase in Revenue: ' + budget['Date'][Revenue.index(Max_Rev)] + ' ($'+str(Max_Rev)+')')

    Min_Rev = min(Revenue)
    print('Greatest Decrease in Revenue: ' + budget['Date'][Revenue.index(Min_Rev)] + ' ($'+str(Min_Rev)+')')

# Textfile output
filename = 'Financial Analysis Budget Data 2_MG.txt'
with open(filename, 'w') as textfile:
    # 
    textfile.write('Financial Analysis\n')
    textfile.write('----------------------------\n')
    textfile.write('Total Month: ' + str(count) + '\n')
    textfile.write('Total Revenue: $' + str(Total) + '\n')
    textfile.write('Greatest Increase in Revenue: ' + budget['Date'][Revenue.index(Max_Rev)] + ' ($'+str(Max_Rev)+')' + '\n')
    textfile.write('Greatest Decrease in Revenue: ' + budget['Date'][Revenue.index(Min_Rev)] + ' ($'+str(Min_Rev)+')')