# import: os, csv
import os
import csv

#path of data file
csvpath = os.path.join("Resources", "election_data.csv")
#set containers/variables
voter_count = 0
candidates = []
#open and read file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #read header
    election_header = next(csvreader)
    #collect total votes & Candidates
    for vote in csvreader:
        voter_count += 1
        if vote[2] not in candidates:
            candidates.append(vote[2])
    #Setup variable to each candidate and reset vote count to Zero
    cand1 = candidates[0]
    cand1_count = 0
    cand2 = candidates[1]
    cand2_count = 0
    cand3 = candidates[2]
    cand3_count = 0
    cand4 = candidates[3]
    cand4_count = 0

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #read header
    election_header = next(csvreader)    
    
    for choice in csvreader:
        if choice[2] == cand1:
            cand1_count += 1
        elif choice[2] == cand2:
            cand2_count += 1
        elif choice[2] == cand3:
            cand3_count += 1
        elif choice[2] == cand4:
            cand4_count += 1

cand1_percentage = round((cand1_count * 100)/ 3521001)
cand2_percentage = round((cand2_count * 100)/ 3521001)
cand3_percentage = round((cand3_count * 100)/ 3521001)
cand4_percentage = round((cand4_count * 100)/ 3521001)

if cand1_percentage > cand2_percentage and cand3_percentage and cand4_percentage:
    winner = cand1
elif cand2_percentage > cand1_percentage and cand3_percentage and cand4_percentage:
    winner = cand2
elif cand3_percentage > cand1_percentage and cand2_percentage and cand4_percentage:
    winner = cand3
elif cand4_percentage > cand1_percentage and cand2_percentage and cand3_percentage:
    winner = cand4

#print the analysis of the Poll data in the terminal
print(f'''
    Results
    ========
    Total Votes: {voter_count}
    ============================================
    {cand1}: {cand1_percentage}% ({cand1_count})
    {cand2}: {cand2_percentage}% ({cand2_count})
    {cand3}: {cand3_percentage}% ({cand3_count})
    {cand4}: {cand4_percentage}% ({cand4_count})
    ============================================
    Winner: {winner}
    =======
    ''')
