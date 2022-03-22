import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

print(csvpath)



with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_votes = 0
    candidates = []
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

print(candidates)




#print(total_votes)