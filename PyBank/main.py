import os
import csv
from typing import Counter

csvpath = os.path.join("Resources", "budget_data.csv")

print(csvpath)

profit_loss_column = []
differences = []

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_months = 0
    total = 0
    for row in csvreader:
        total_months += 1
        total += int(row[1])
        profit_loss_column.append(int(row[1]))
# print(total_months)
# print(total)


    for x in range(85):
        difference = profit_loss_column[x+1] - profit_loss_column[x]
        differences.append(difference)
print(differences)




# cleaned_csv = zip(date, profit_losses)
# # Set variable for output file
# output_file = os.path.join("main_final.csv")
# #  Open the output file
# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)
#     # Write the header row
#     writer.writerow(["Date", "Profit/Losses"])
#     # Write in zipped rows
#     writer.writerows(cleaned_csv)


    # total_profit_loss = sum(column2 for row in csvreader)
    # print(total_profit_loss)