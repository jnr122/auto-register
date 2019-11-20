import re

# open the text file with the raw schedule into variable raw_data
with open("aux/schedule_page.txt","r") as file:
    raw_data = file.read()

rows = re.split("\n",raw_data)
for i in range(len(rows)):
    rows_i_ = rows[i][0:4]
    if rows_i_ != "<td " and rows_i_ != "<tr>" and rows_i_ != "</tr":
        rows[i] = 'X'

rows = [x for x in rows if x != 'X']


all_classes = []
j = 0
for i in range(len(rows)):
    if rows[i] == "<tr>" and rows[i+1][0:3] == "<td":
        individual_class = []
        k=1
        while rows[i+k][0:3] == "<td":
            individual_class.append(rows[i + k])
            k += 1
        all_classes.append(individual_class)
        j += 1

all_classes_clean = all_classes #make a copy to put the clean data in (preserves the odd size of the lists)
for i in range(len(all_classes)):
    for j in range(len(all_classes[i])):
        all_classes_clean[i][j] = re.sub('<.*?>', '',all_classes[i][j])


with open('aux/classes.txt', 'w') as f:
    for item in all_classes_clean:
        f.write("%s\n" % item)



