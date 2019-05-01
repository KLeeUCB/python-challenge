import os
import csv

budget_file = os.path.join("Resources", "budget_data.csv")
budget_output = budget_file = os.path.join("analysis", "budget_analysis.csv")

# The total number of months included in the dataset
total_months = 0

# The total net amount of "Profit/Losses" over the entire period
total_net = 0

# The average change in "Profit/Losses" between months over the entire period
month_change = []
net_change_list = []

# The greatest increase in profits (date and amount) over the entire period
increase = ["", 0]

# The greatest decrease in losses (date and amount) over the entire period
decrease = ["", 9999999]

# Open and read csv
with open(budget_file, newline="") as csvfile:

    csvreader = csv.reader(csvfile)

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    # Read through each row of data after the header
    for row in csvreader:

        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        month_change = .append(row[0])

        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change

        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg: .2f}\n"
    f"Greatest Profit increase: ${increase[0]}\n"
    f"Greatest Profit decrease: ${decrease[0]}\n"
)

print(output)


