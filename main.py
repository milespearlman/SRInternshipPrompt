import json

file = open('data.json', 'r')
data = json.load(file)

outputArray = []

# Create table (this is really an array of arrays)
for team in data:
    winsAgainst = []
    for opponent in data:
        # Obviously no wins against themself
        if opponent == team:
            winsAgainst.append("--")
        else:
            winsAgainst.append(data[team][opponent]['W'])
    outputArray.append(winsAgainst)

teams = list(data.keys())

# Print table
print("| Tm|", end = "")
for opponent in teams:
    print(f"{opponent}|", end="")
print()
for i in range(len(teams)):
    print(f"|{teams[i]}|", end="")
    for k in range(len(teams)):
        print(f"{outputArray[i][k]:>3}|", end="")
    print()

file.close()