import os
import csv

pypoll = os.path.join('ref', 'election.csv')

#def vote_percentage(election_data):
    #name = str(election_data[2])

with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #couting number of votes count
    data = list(csvreader)
    row_count = len(data) 
    
    print(row_count)
    
    #setting total vote count here
    khan_count = [0]
    correy_count = [0]
    li_count = [0]
    otooley_count = [0]
    
    #skip the first row since this is the header
    header = next(csvreader)
    
    #go through each row, if third column says Khan, add 1 to khan_count, etc
    for row in csvreader:
        if row[2] == "Khan":
            khan_count += 1
        elif row[2] == "Correy":
            correy_count += 1
        elif row[2] == "Li":
            li_count += 1
        else:
            otooley_count += 1
            
    #will need to calculate the percent
    khan_percent = khan_count/row_count
    correy_percent = correy_count/row_count
    li_percent = li_count/row_count
    otooley_percent = otooley_count/row_count
    
    print("Election Results")
    print("_________________________")
    print(f"Total Votes: {str(row_count)}")
    print(f"Khan: (" + str(khan_percent) + ")" + "(" + str(khan_count) + ")")
    print(f"Correy: (" + str(correy_percent) + ")" + "(" str(correy_count) + ")")
    print(f"Li: (" + str(li_percent) ")" + "(" str(li_count) + ")")
    print(f"O'Tooley: (" + str(otooley_percent) ")" + "(" str(otooley_count) + ")")
    print("_________________________")
    print(f"Winner: {winnername}")
    print("_________________________")