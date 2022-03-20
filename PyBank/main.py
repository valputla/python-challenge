import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

print(csvpath)

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
      
    total_months = sum(1 for row in csvreader)
    print(total_months)
    #86 is the total

    
    # total_profit_losses = sum(row[1] for row in csvreader)
    # print(total_profit_losses)

    # sorted_dates = sorted(row[0] for row in csvreader)
    # print(sorted_dates)

    for row in csvreader:
        total_profit_losses = 0
        total_profit_losses = total_profit_losses + row[1]
        print(total_profit_losses)


    for row in csvreader:
        total = sum(row[1])
        print(total)

    for row in csvreader:
        print(row[1])






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