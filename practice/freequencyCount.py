myStr = "Bangladesh"

freequency = {}

for item in myStr:
    if item in freequency:
        freequency[item] += 1
    else:
        freequency[item] = 1


for i,count in freequency.items():
    print(f"{i}:{count}")