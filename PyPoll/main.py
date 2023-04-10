import csv
import os

#locate the path of the file
csvpath=os.path.join('/Users/cassie/Documents/MONASH/Activity/Starter_Code week 3/Python-Challenge/PyPoll/Resources/election_data.csv')

# Open the CSV file
with open(csvpath, 'r') as csvfile:

    # Read the CSV file into a dictionary
    reader = csv.DictReader(csvfile)

    # Initialize variables to store the total number of votes and the vote counts for each candidate
    total_votes = 0
    candidate_votes = {}

    # Loop through each row in the CSV file
    for row in reader:

        # Increment the total number of votes
        total_votes += 1

        # Get the candidate name from the row
        candidate_name = row['Candidate']

        # If this is the first vote for the candidate, initialize their vote count to 1
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1

        # Otherwise, increment their vote count by 1
        else:
            candidate_votes[candidate_name] += 1

    #print Election Result
    print('Election Results\n')
    print('-------------------------\n')

    # Print the total number of votes cast
    print(f'Total Votes: {total_votes}'+'\n')
    print('-------------------------\n')

    # Calculate the percentage of votes each candidate won and print the results
    for candidate_name, votes in candidate_votes.items():
        vote_percentage = votes / total_votes * 100
        print((f'{candidate_name}: {vote_percentage:.3f}% ({votes})'))
        
    # Find the winner of the election based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)
    print('-------------------------\n')
    print(f'Winner: {winner}'+'\n')
    print('-------------------------\n')

    # Define the path to the output text file
output_file = os.path.join('/Users/cassie/Documents/MONASH/Activity/Starter_Code week 3/Python-Challenge/PyPoll/analysis/election_results.txt')

# Write the analysis results to the output text file
with open(output_file, 'w') as f:
    f.write('Election Results\n')
    f.write('------------------------\n')
    f.write(f'Total Votes: {total_votes}'+'\n')
    f.write('-------------------------\n')
    for candidate_name, votes in candidate_votes.items():
        vote_percentage = votes / total_votes * 100
        f.write(f'{candidate_name}: {vote_percentage:.3f}% ({votes})'+'\n')
    f.write('-------------------------\n')
    f.write(f'Winner: {winner}'+'\n')
    f.write('-------------------------\n')
    
# Print a message to confirm that the results have been exported
print(f"The results have been exported to {output_file}")