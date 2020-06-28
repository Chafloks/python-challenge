import os
import csv
K=0
C=0
L=0
O=0
mx=0
csvpath1 = os.path.join("Resources","election_data.csv")
csvpath2 = os.path.join("Analysis","Election Results.txt")
with open(csvpath1) as csvfile:
    csv_header = next(csvfile)
    data = [row for row in csv.reader(csvfile)]
    total=len(data)
for i in data:
    if i[2] == "Khan":
        K+= 1
    elif i[2] == "Correy":
        C+=1
    elif i[2] == "Li":
        L+=1
    elif i[2] == "O'Tooley":
        O+=1
results=[K,C,L,O]
if max(results) == K:
    winner="Khan"
elif max(results) == C:
    winner="Correy"
elif max(results) == L:
    winner="Li"
if max(results) == O:
    winner="O'Tooley"
print("Election Results\n-------------------------\nKhan: ",(K/total) * 100," (",K,")\nCorrey: ",(C/total) * 100," (",C,")\nLi: ",(L/total) * 100,"(",L,")\nO'Tooley: ",(O/total) * 100,"(",O,")\n-------------------------\nWinner: ",winner,"\n-------------------------")
file1 = open(csvpath2,"w")
L=["Election Results\n-------------------------\nKhan: ",str((K/total) * 100)," (",str(K),")\nCorrey: ",str((C/total) * 100)," (",str(C),")\nLi: ",str((L/total) * 100),"(",str(L),")\nO'Tooley: ",str((O/total) * 100),"(",str(O),")\n-------------------------\nWinner: ",winner,"\n-------------------------"]
file1.writelines(L)