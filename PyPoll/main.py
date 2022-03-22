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
    charlie = []
    total_votes_CCS = 0
    total_votes_DD = 0
    total_votes_RAD = 0
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Charles Casper Stockham":
            total_votes_CCS += 1
print(total_votes_CCS)






#print(total_votes)
#print(candidates)


# print("Election Results")
# print("-----------------------------")
# print(f"Total Votes: {total_votes}")
# print("-----------------------------")
# print(f"Charles Casper Stockham: ")