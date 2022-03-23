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
#
max_difference = ["Aug-16", 1862002]
min_difference = ["Feb-14", -1825558]

# Set variable for output file
output_file_final= os.path.join("main_final.txt")

#  Open the output file
with open(output_file_final, "w") as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("----------------------")
    f.write("\n")
    f.write(f"Total Months: {total_months}")
    f.write("\n")
    f.write("----------------------")
    f.write("\n")
    f.write(f"Total: ${total}")
    f.write("\n")
    f.write("Average Change: $" + str(percent))
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {max_difference}")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {min_difference}")
   
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print("Average Change: $" + str(percent))
print(f"Greatest Increase in Profits: {max_difference}")
print(f"Greatest Decrease in Profits: {min_difference}")



    
   






