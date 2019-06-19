import os
import csv

pybank = os.path.join('ref', 'budget data.csv')

 
with open(pybank, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    #couting total months
    #data = list(csvreader)
    #ow_count = len(data)        
          
    #setting list up for variables, skipping first line due to it being the header 
    header = next(reader)
    profit = []
    month = []
    profit_change = []
    
    #profit.appen(float(row[1]))
    #date.append(row[0])
    
    #calculating sum of profits 
    for row in reader:
        profit.append(float(row[1]))
        month.append(row[0])
    
    print("total months:", len(month))
    print("Total Profit: $", sum(profit))

    for i in range(1, len(profit)):
        profit_change.append(profit[i] - profit[i-1])
        avg_profit_change = sum(profit_change)/len(profit_change)
        
        max_profit_change = max(profit_change)
        
        min_profit_change = min(profit_change)
        
        max_profit_change_month = str(month[profit_change.index(max(profit_change))])
        min_profit_change_month = str(month[profit_change.index(min(profit_change))])
        
    print("Greatest Increse in Profit:", max_profit_change_month, "($", max_profit_change,")")
    print("Greatest Decrease in Profit:", min_profit_change_month, "($", min_profit_change,")")
       
    #print(f"Total Months: {str(row_count)}")
    #print(f"Total: {str(net_total)}) 
    
    #display results together    
    print("Financial Analysis")
    print("_______________________________")
   
    print("total months:", len(month))
    print("Total Profit: $", sum(profit))
    print("Average Profit Change: $", round(avg_profit_change))
    print("Greatest Increse in Profit:", max_profit_change_month, "($", max_profit_change,")")
    print("Greatest Decrease in Profit:", min_profit_change_month, "($", min_profit_change,")")
 