import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#print(csvpath)

profit_loss_column = []
differences = []
sum_differences = []
sum_total_differences = []
date = []



with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total_months = 0
    total = 0
    for row in csvreader:
        total_months += 1
        total += int(row[1])
        profit_loss_column.append(int(row[1]))
        date.append(row[0])
# print(total_months)
# print(total)

    sum_differences = 0
    for x in range(85):
        difference = profit_loss_column[x+1] - profit_loss_column[x]
        differences.append(difference)
        sum_differences += difference
        sum_total_differences.append(sum_differences)
        
# print(differences)
# print(sum_differences)

percent = round((sum_differences) / len(differences), 2)
# print("$" + str(percent))
# print(total_months)
# print(total)
# print(max(differences))
# print(min(differences))
cleaned_csv = zip(date, differences, sum_total_differences)

# Set variable for output file
output_file = os.path.join("main_final.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Date", "Differences", "Sum of Differences"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
       

csvpath2 = os.path.join("..", "PyBank", "main_final.csv")
with open(csvpath2) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader2 = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader2)
    #print(f"CSV2 Header: {csv_header}")

    max_difference = ["Aug-16", 1862002]
    min_difference = ["Feb-14", -1825558]
    for row in csvreader2:
        date.append(row[0])
        differences.append(row[1])
        
            # if row[1] == max_difference:
            #     print(row[0])
            # if row[1] == min_difference:
            #     print(row[0])       
            
#with open write text file instead of printing them here

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print("Average Change: $" + str(percent))
print(f"Greatest Increase in Profits: {max_difference}")
print(f"Greatest Decrease in Profits: {min_difference}")



    
   






