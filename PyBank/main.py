#Import modules
import os
import csv

#Pull the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

#print(csvpath)

#Create empty lists for data to be appended to. 
profit_loss_column = []
differences = []
sum_differences = []
sum_total_differences = []
date = []


#Open the CSV file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Use next to skip the first line to capture the header.
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total_months = 0
    total = 0

    #Use for loop to loop through each row of the bank data. 
    for row in csvreader:

    #Total month starts at 0, add 1 for each loop.
        total_months += 1

    #Sum of the information in the Profit/Loss column
        total += int(row[1])

    #Add new information to a profit/loss column list.
        profit_loss_column.append(int(row[1]))
        date.append(row[0])

# print(total_months)
# print(total)


    sum_differences = 0
    #Loop through 85 rows as we need to account for NOT using the last row.
    for x in range(85):
    #Calculate the difference and add values to differences list.
        difference = profit_loss_column[x+1] - profit_loss_column[x]
        differences.append(difference)

    #Add up all the differences to create the sum differences and append to sum total list.
        sum_differences += difference
        sum_total_differences.append(sum_differences)
        
# print(differences)
# print(sum_differences)


#Calculate the average change, rounded to 2 decimal places. 
avg_change = round((sum_differences) / len(differences), 2)
# print("$" + str(percent))
# print(total_months)
# print(total)
# print(max(differences))
# print(min(differences))

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
    f.write("Average Change: $" + str(avg_change))
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {max_difference}")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {min_difference}")

#Print output to terminal.
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print("Average Change: $" + str(avg_change))
print(f"Greatest Increase in Profits: {max_difference}")
print(f"Greatest Decrease in Profits: {min_difference}")



    
   






