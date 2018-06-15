## PyPoll
import os
import csv

run = "y"
while (run=="y"):
    filerun = int(input("What number file would you like to run this on? "))
    print("")
# Read in the data
    csvpath = os.path.join("poll_raw_data", "election_data_%d.csv" %filerun)

# The total number of votes cast, and create lists for candidates and their votes recweived
    Total_votes = 0
    Candidates = []
    Candidate_votes = []

    with open(csvpath, newline="") as csvfile:
        poll_data = csv.reader(csvfile, delimiter=",")
        firstline = True
        for row in poll_data:
            if firstline:
                firstline = False
                continue
            Total_votes += 1
            if row[2] not in Candidates:
                Candidates.append(row[2])
                Candidate_votes.append(1)
            else:
                inx = Candidates.index(row[2])
                Candidate_votes[inx] += 1

# Calculate the percentage of votes received by each candidate
    Vote_percentage = []
    Vote_percentage = [(can/Total_votes)*100 for can in Candidate_votes]

# Find the winner
    winning_index = Vote_percentage.index(max(Vote_percentage))
    winner = Candidates[winning_index]

# Print the Results to Terminal
    print("...")
    print("Election Results")
    print("-" * 20)
    print("Total Votes: " + str(Total_votes))
    print("-" * 20)
    Can_length = len(Candidates)
    for x in range(0, Can_length):
        print(f"{Candidates[x]}: {'%.1f'%Vote_percentage[x]}% ({Candidate_votes[x]})")
    print("-" * 20)
    print("Winner: " + str(winner))
    print("...")  

## Print the results out to a text file
    text_file = open("poll_output_%d.txt" %filerun, "w")
    with open("poll_output_%d.txt" %filerun, "w") as text_file:
        print("...", file = text_file)
        print("Election Results", file = text_file)
        print("-" * 20, file = text_file)
        print("Total Votes: " + str(Total_votes), file = text_file)
        print("-" * 20, file = text_file)
        Can_length = len(Candidates)
        for x in range(0, Can_length):
            print(f"{Candidates[x]}: {'%.1f'%Vote_percentage[x]}% ({Candidate_votes[x]})", file = text_file)
        print("-" * 20, file = text_file)
        print("Winner: " + str(winner), file = text_file)
        print("...", file = text_file)  
    run = input("Would you like to run this on another file? (y|n) ")
    print("")