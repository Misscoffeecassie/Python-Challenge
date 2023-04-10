import os
import csv

#define the file path
#file_path = os.path.join('Resources', 'budget_data.csv')
file_path="/Users/cassie/Documents/MONASH/Activity/Starter_Code week 3/Python-Challenge/PyBank/Resources/budget_data.csv"
# Define variables to hold the results
total_month=0
net_total_profit=0
previous_profit=0
profit_change=0
profit_change_list=[]
greatest_increase={"date": "", "amount": 0}
greatest_decrease={"date": "", "amount": 0}


# Open the CSV file and loop through the rows
with open (file_path,'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    header=next(csv_reader) # skip the head row

    for row in csv_reader:
        total_month = total_month +1

        # Add the profit/loss to the net total
        net_total_profit = int(row[1])+ net_total_profit 

        # Calculate the change in profit/loss from the previous row
        current_profit = int(row[1])

        if total_month > 1:
            profit_change = current_profit - previous_profit
            profit_change_list.append(profit_change)


            # Check if this is the greatest increase or decrease
            if profit_change > greatest_increase["amount"]:
                greatest_increase["amount"] = profit_change
                greatest_increase["date"] = row[0]
            elif profit_change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = profit_change
                greatest_decrease["date"] = row[0]

                # Update the previous profit/loss
        previous_profit = current_profit

# Calculate the average change in profit/loss
average_change = sum(profit_change_list) / len(profit_change_list)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${net_total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Define the path to the output text file
output_file = os.path.join('/Users/cassie/Documents/MONASH/Activity/Starter_Code week 3/Python-Challenge/PyBank/analysis/financial_analysis.txt')

# Write the analysis results to the output text file
with open(output_file, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("---------------------------\n")
    f.write(f"Total Months: {total_month}" +"\n")
    f.write(f"Total: ${net_total_profit}"+"\n")
    f.write(f"Average Change: ${average_change:.2f}"+"\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})"+"\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"+"\n")
    
# Print a message to confirm that the results have been exported
print(f"The results have been exported to {output_file}")
