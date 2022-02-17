# Check percent sign in the file
from faulthandler import dump_traceback


check_percent = False
# Check if len is 0
len_p = True
# Store the project percents

percent = []
duration = []
complete = []

with open('./mangantt.txt') as f:
    for line in f:
        # Exclude spaces
        striped = line.strip()
        splited = striped.split()

        # Percent complet
        if len(striped) != 0  and "%" in striped:
            percent.append(float(splited[2].replace('%', '')))
        
        # Duration for tasks
        if len(striped) != 0  and "lasts" in striped:
            value_index = splited.index("lasts")
            duration.append(float(splited[value_index + 1]))

for i, j in zip(percent, duration):
    comp = i * 0.01 * j
    complete.append(comp)

total_project_days = sum(duration)
total_project_complete_days = sum(complete)

percent_complete = total_project_complete_days * 100 / total_project_days
print(percent_complete)
print(sum(duration))