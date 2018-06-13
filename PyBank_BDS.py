### PyBank
import os
import csv  

## Read in the data
csvpath = os.path.join("bank_raw_data", "budget_data_2.csv")

#Loop through the data and read it into lists for Months and Revenue
Months = []
Revenue = []
Revenue_change = []

with open(csvpath, newline="") as csvfile:
    bank_data = csv.reader(csvfile, delimiter=",")
    firstline = True
    for row in bank_data:
        if firstline:
            firstline = False
            continue
        Months.append(row[0])
        Revenue.append(row[1])
        
#Calculate the number of Months, turn revneue into integers
Num_rows = len(Months)
Revenue_nums = [int(rev) for rev in Revenue]
Tot_Revenue = sum(Revenue_nums)

#Create the Revenue Change list
for i in range(1, Num_rows):
    Revenue_change.append(Revenue_nums[i] - Revenue_nums[i-1])

## Get the average
Average_change = sum(Revenue_change) / len(Revenue_change)

##Get the min and the max of the revenues changes
Min_rc = min(Revenue_change)
Max_rc = max(Revenue_change)

### revenue change is going to have 40 entries, from 0 to 39, each entry will belong to corresponding row + 1
Min_inx = int(Revenue_change.index(Min_rc)) + 1
Max_inx = int(Revenue_change.index(Max_rc)) + 1
    
#Match revenue changes to the correct month    
Min_month =  Months[Min_inx]
Max_month = Months[Max_inx]

#print to terminal
print("Financial Analysis")
print("-" * 20)
print("Total Months: " + str(Num_rows))
print("Total Revenue: $" + '%.2f'%Tot_Revenue)
print("Average Revenue Change: $" + '%.2f'%Average_change)
print("Greatest Increase in Revenue: " + str(Max_month) + " ($" + '%.2f'%Max_rc + ")")
print("Greatest Decrease in Revenue: " + str(Min_month) + " ($" + '%.2f'%Min_rc + ")")
print("...")  

## Print the results out to a text file
text_file = open("bank_output.txt", "w")
with open("output.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("-" * 20, file = text_file)
    print("Total Months: " + str(Num_rows), file = text_file)
    print("Total Revenue: $" + '%.2f'%Tot_Revenue, file = text_file)
    print("Average Revenue Change: $" + '%.2f'%Average_change, file = text_file)
    print("Greatest Increase in Revenue: " + str(Max_month) + " ($" + '%.2f'%Max_rc + ")", file = text_file)
    print("Greatest Decrease in Revenue: " + str(Min_month) + " ($" + '%.2f'%Min_rc + ")", file = text_file)
    print("...", file = text_file)