import csv
from collections import OrderedDict
from operator import itemgetter

csvpath = "election_data.csv"
output_path = "Election_Analysis.txt"

total_votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


with open(csvpath) as election_data:
    csvreader = csv.DictReader(election_data)

    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(total_votes))
    print("-------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


with open(output_path, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(total_votes))