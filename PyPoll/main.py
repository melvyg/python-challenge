import os

path = os.path.dirname(os.path.realpath(__file__))

election_data2 = "election_data_2.csv"

import csv
with open(election_data2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    poll_dict = {}

    # Construct Dictionary and count of votes for each candidate

    for row in csvreader:
        if row[2] in poll_dict.keys():
            poll_dict[row[2]] += 1
        else:
            poll_dict[row[2]] = 1
    poll_dict.pop('Candidate')

    # Count Total votes

    TotalVotes = 0
    for value in poll_dict.values():
        TotalVotes += value

winner = max(zip(poll_dict.values(), poll_dict.keys()))[1]
    
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(TotalVotes))
print('-------------------------')
for key, value in poll_dict.items():
    print(key + ': ' + str(round(((value/TotalVotes)*100), 1)) + '% ' + '(' + str(value) + ')')
print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')

# Textfile output
filename = 'Election Data 2 Output.txt'
with open(filename, 'w') as textfile:
    textfile.write('Election Results\n')
    textfile.write('-------------------------\n')
    textfile.write('Total Votes: ' + str(TotalVotes) + '\n')
    textfile.write('-------------------------\n')
    for key, value in poll_dict.items():
        textfile.write(key + ': ' + str(round(((value/TotalVotes)*100), 1)) + '% ' + '(' + str(value) + ')' + '\n')
    textfile.write('-------------------------\n')
    textfile.write(('Winner: ' + winner + '\n'))
    textfile.write('-------------------------')
