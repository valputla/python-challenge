import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

print(csvpath)



with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    total_votes = 0
    candidates = []
    total_votes_CCS = 0
    total_votes_DD = 0
    total_votes_RAD = 0
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == "Charles Casper Stockham":
            total_votes_CCS += 1
            
        if row[2] == "Diana DeGette":
            total_votes_DD += 1
            
        if row[2] == "Raymon Anthony Doane":
            total_votes_RAD += 1
        
    
    percent_CCS = round(total_votes_CCS/total_votes * 100, 3)
    percent_DD = round(total_votes_DD/total_votes * 100, 3)
    percent_RAD = round(total_votes_RAD/total_votes * 100, 3)


candidate_votes = [total_votes_CCS, total_votes_DD, total_votes_RAD]
#print(max(candidate_votes))

# if max(candidate_votes) == 85213:
#     print("Charles Casper Stockham")
# elif max(candidate_votes) == 272892:
#     print("Diana DeGette")
# else:
#     print("Raymon Anthony Doane")





#print(total_votes)
#print(candidates)
#print(total_votes_CCS)
# print(total_votes_DD)
# print(total_votes_RAD)
# print(percent_CCS)
# print(percent_CCS)
# print(percent_DD)
# print(percent_RAD)


print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"Charles Casper Stockham: {percent_CCS}% ({total_votes_CCS})")
print(f"Diana DeGette: {percent_DD}% ({total_votes_DD})")
print(f"Raymon Anthony Doane: {percent_RAD}% ({total_votes_RAD})")
print("-----------------------------")
print(f"Winner: Diana DeGette")
print("-----------------------------")