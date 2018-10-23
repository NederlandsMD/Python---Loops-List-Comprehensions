# Python Exercises - Arrays, Loops, and Dynamic File Writing

The two exercises in this repository use Python to read through bank statements and polling data, respectively. 

# Bank Statements

This script analyzes the financial records of a fictional company, and prints out a summary to a text file. The file includes the number of months in the dataset, total revenue gained, average change in revenue between months over the time period, and greatest increase and decrease in revenue (date and amount).

The script is written so that users can input the budget sheet number, then the program finds the correct file and runs the analysis accordingly. 

This script makes use of while loops, for loops, appending to arrays, list comprehensions, functions such as sum() and len(), identifies array entries by their index ((Min_inx = int(Revenue_change.index(Min_rc)) + 1)).

It also dynamically reads in a file:
csvpath = os.path.join("bank_raw_data", "budget_data_%d.csv" %filerun)

Uses specific formatting to modify output:
print("Greatest Increase in Revenue: " + str(Max_month) + " ($" + '%.2f'%Max_rc + ")")

And dynamically writes the output to a text file:
text_file = open("bank_output_%d.txt" %filerun, "w")

# Polling Data

This script creates a python script to analyze raw vote data from a fictional small town and return an analysis with number of votes cast, a list of candidates who received votes, percentage of votes won by each candidate, total number of votes won by each candidate, and winner of the election based on popular vote.

The script returns the output both to the terminal and to a dynamically written text file.

The script makes use of while loops to dynamically read in raw polling data, dynamically adds new candidates to the candidate array if they receive votes, then calculates the vote percentage of each candidates and finds the winning candidate.           
    winning_index = Vote_percentage.index(max(Vote_percentage))
    winner = Candidates[winning_index]
