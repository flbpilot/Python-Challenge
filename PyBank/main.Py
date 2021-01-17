# import the csv file
import os
import csv
filepath = os.path.join("Resources", "budget_data.csv")

# open the csv
with open(filepath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)

    #create Variables, Containers for the list of months , monthly profits , and profit changes
    Months = 0
    Total_Profit = 0
    Average_Revenue_Change = 0
    Total_Change = 0
    Date = []
    Revenue = []
    Revenue_Change = []
    Max_Increase_Change = 0
    Max_Decrease_Change = 0
    Max_Increase_Date = None
    Max_Decrease_Date = None

    # create loop to find number of Months
    for row in csvreader:
        Months += 1

        # find Total Profit
        Total_Profit = Total_Profit + int(row[1])

        # append each column
        Date.append(row[0])
        Revenue.append(row[1])

    # find the Change Average
    for i in range(len(Revenue)-1):
        Total_Change = int(Revenue[i]) - int(Revenue[i-1])
        Revenue_Change.append(Total_Change)
    Average_Revenue_Change = (Total_Change/Months)

    # find the largest incease & Dicrease
    Max_Increase_Change = max(Revenue_Change)
    Max_Decrease_Change = min(Revenue_Change)

    # put the dates with the maxs
    Max_Increase_Date = str(Date[Revenue_Change.index(max(Revenue_Change))])
    Max_Decrease_Date = str(Date[Revenue_Change.index(min(Revenue_Change))])

    # print results
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(Months))
    print("Total: " + "$" + str(Total_Profit))
    print("Average Change: " + "$" + str(round(Average_Revenue_Change)))
    print("Largest Monthly Increase: " + str(Max_Increase_Date) + " $" + str(Max_Increase_Change))
    print("Largest Monthly Decrease: " + str(Max_Decrease_Date) + " $" + str(Max_Decrease_Change))

    