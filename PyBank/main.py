import csv

csvpath = "budget_data.csv"
output_path = "Financial_Analysis.txt"

total_months = 0
net_total = 0

previous_record = None
current_record = None
PnL_change = None
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
counter = 2

PnL_changes = []

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:

        total_months = total_months + 1
        net_total = net_total + int(row["Profit/Losses"])
  
        if counter == 2:
            previous_record = int(row["Profit/Losses"])
        else:
            current_record = int(row["Profit/Losses"])
            PnL_change = current_record - previous_record
            PnL_changes.append(PnL_change)

            if (PnL_change > greatest_increase[1]):
                greatest_increase[1] = PnL_change
                greatest_increase[0] = row["Date"]

            if (PnL_change < greatest_decrease[1]):
                greatest_decrease[1] = PnL_change
                greatest_decrease[0] = row["Date"]
            previous_record = current_record
        counter = counter + 1
        
    revenue_avg = sum(PnL_changes) / len(PnL_changes)
    
    print()
    print()
    print()
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(net_total))
    print("Average Change: " + "$" + str(round(sum(PnL_changes) / len(PnL_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    

with open(output_path, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(net_total))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(PnL_changes) / len(PnL_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
