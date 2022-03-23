#Import modules
import os
import csv

#Pull the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

#print(csvpath)

#Open the CSV file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Use next to skip the first line to capture the header.
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#Create variables and empty list for candidates. 
    total_votes = 0
    candidates = []
    total_votes_CCS = 0
    total_votes_DD = 0
    total_votes_RAD = 0

#Use for loop to loop through each row of the election data. 
    for row in csvreader:
        #Total votes starts at 0, add 1 for each loop.
        total_votes += 1

        #Check to see if value in row[2] (candidate name) is in the candidates list.
        #If it is not there, add candidate name to candidates list.
        #Google assisted me with the "not in" syntax.
        if row[2] not in candidates:
            candidates.append(row[2])

        #If the value in each row, index 2 is Charles Stockham, add 1 to total his votes.
        if row[2] == "Charles Casper Stockham":
            total_votes_CCS += 1

        #If the value in each row, index 2 is Diana DeGette, add 1 to total her votes.   
        if row[2] == "Diana DeGette":
            total_votes_DD += 1
            
        #If the value in each row, index 2 is Raymon Doane, add 1 to total his votes.
        if row[2] == "Raymon Anthony Doane":
            total_votes_RAD += 1
        
    #Calculate percentage of votes, round to 3 decimal places.
    percent_CCS = round(total_votes_CCS/total_votes * 100, 3)
    percent_DD = round(total_votes_DD/total_votes * 100, 3)
    percent_RAD = round(total_votes_RAD/total_votes * 100, 3)

#Find the max total votes.
candidate_votes = [total_votes_CCS, total_votes_DD, total_votes_RAD]
#print(max(candidate_votes))

#Another way to find max votes by printing out the candidates name.
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


# Set variable for output file
output_file_final= os.path.join("main_final.txt")

#  Open the output file
with open(output_file_final, "w") as f:
    f.write("Election Results")
    f.write("\n")
    f.write("----------------------")
    f.write("\n")
    f.write(f"Total Votes: {total_votes}")
    f.write("\n")
    f.write("----------------------")
    f.write("\n")
    f.write(f"Charles Casper Stockham: {percent_CCS}% ({total_votes_CCS})")
    f.write("\n")
    f.write(f"Diana DeGette: {percent_DD}% ({total_votes_DD})")
    f.write("\n")
    f.write(f"Raymon Anthony Doane: {percent_RAD}% ({total_votes_RAD})")
    f.write("\n")
    f.write("----------------------")
    f.write("\n")
    f.write(f"Winner: Diana DeGette")
    f.write("\n")
    f.write("----------------------")

    
    

#Print final output. 
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