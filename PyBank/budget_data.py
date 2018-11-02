import os
import csv

budgetDataCSV = os.path.join("budget_data.csv")

Months = []
profitLoss = []
profitLossChange = []

with open(budgetDataCSV, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for i in csvreader:
        Months.append(i[0])
        profitLoss.append(int(i[1]))
    for j in range(1, len(profitLoss)):
        profitLossChange.append((profitLoss[j])-(profitLoss[j-1]))

maxIncrease = max(profitLossChange)
maxDecrease = min(profitLossChange)
maxIncreaseMonth = profitLossChange.index(max(profitLossChange)) + 1
maxDecreaseMonth = profitLossChange.index(min(profitLossChange)) + 1

print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {len(Months)}")
print(f"Total:  ${sum(profitLoss)}")
print(f"Average Change: ${round(sum(profitLossChange)/len(profitLossChange),2)}")
print(f"Greatest Increase in Profits: {Months[maxIncreaseMonth]} (${(str(maxIncrease))})")
print(f"Greatest Decrease in Profits: {Months[maxDecreaseMonth]} (${(str(maxDecrease))})")