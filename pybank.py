import os
import csv

pybank = os.path.join('ref', 'budget data.csv')

with open(pybank, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # tell code to read the header row first, setting variables
    header = next(csvreader)
   
    rows = 0
    total = 0
    Profit = 0
    Loss = 0
    row_profit = 0
    row_loss = 0
    Max = 0
    Min = 0
    
    #to find the average of the data?
    PL_change = 0
    Total_PL_list = []
    Month_change = 0
    PL_change_list = []
    Total_months_list = []
    current_PL = 0
    last_PL = 0
    
    
    for row in csvreader:
        rows += 1

        total = total + int(row[1])

        if (int(row[1]) > 0):
            Profit = Profit + int(row[1])
            row_profit += 1
        else:
            Loss = Loss + int(row[1])
            row_loss += 1
        
        Total_months_list.append(row[0])
        Total_PL_list.append(int(row[1]))
        
        if (int(row[1]) > Max):
            Max = int(row[1])
            Month_max = row[0]
        elif (int(row[1]) < Min):
            Min = int(row[1])
            Month_min = row[0]

    for i in range(len(Total_PL_list) - 1):
        PL_change_list.append(Total_PL_list[i + 1] - Total_PL_list[i])

    Average_change = (sum(PL_change_list)) / (len(PL_change_list))


# Print the analysis
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {str(rows)}")
print(f"Total: ${str(total)}")
print(f"Average Change: ${str('%.2f' % Average_change)}")
print(f"Greatest Increase in Profits: {Month_max} (${str(Max)})")
print(f"Greatest Decrease in Profits: {Month_min} (${str(Min)})")
        
results_file = ('C:\\Users\\vangs\\Desktop\\homework\\Summary.txt')

with open(results_file, 'w') as file:
    file.write("Financial Analysis")
    file.write("-----------------------")
    file.write(f"Total Months: {str(rows)} ")
    file.write(f"Total: ${str(total)}")
    file.write(f"Average Change: ${str('%.2f' % Average_change)}")
    file.write(f"Greatest Increase in Profits: {Month_max} (${str(Max)})")
    file.write(f"Greatest Decrease in Profits: {Month_min} (${str(Min)})")