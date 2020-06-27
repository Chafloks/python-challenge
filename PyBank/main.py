import os
import csv

total=0
count=0
change=[]
big=0
small=0
spot1=0
spot2=0
csvpath1 = os.path.join("Resources","budget_data.csv")
csvpath2 = os.path.join("Analysis","Financial Analysis.txt")
with open(csvpath1) as csvfile:
    csv_header = next(csvfile)
    data = [row for row in csv.reader(csvfile)]
    for list in data:
        for number in list[1::2]:
            total = total + int(number)
            count = count + 1
            change.append(int(number))
    v = [change[i+1]-change[i] for i in range(len(change)-1)]
    avg="{:.2f}".format(sum(v)/len(v))
    for i, j in enumerate(v):
        if big is None or j > big:
             big = j
             spot1 = i

    for i, j in enumerate(v):
        if small is None or j < small:
             small = j
             spot2 = i
    print("Financial Analysis\n----------------------------\nTotal Month: ",count,"\nTotal: $",total,"\nAverage Change: ",avg,"\nGreatest Increase in Profits: ",data[spot1+1][0],"($",big,")","\nGreatest Increase in Profits: ",data[spot2+1][0],"($",small,")")
    file1 = open(csvpath2,"w")
    L=["Financial Analysis\n----------------------------\nTotal Month: ",str(count),"\nTotal: $",str(total),"\nAverage Change: ",str(avg),"\nGreatest Increase in Profits: ",str(data[spot1+1][0]),"($",str(big),")","\nGreatest Increase in Profits: ",str(data[spot2+1][0]),"($",str(small),")"]
    file1.writelines(L)