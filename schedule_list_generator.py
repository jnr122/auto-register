import re

# open the text file with the raw schedule into variable raw_data
with open("schedule_page.txt","r") as file:
    raw_data = file.read()

rows = re.split("\n",raw_data)
# print(rows[300][0:3])
for i in range(len(rows)):
    rows_i_ = rows[i][0:4]
    if rows_i_ != "<td " and rows_i_ != "<tr>" and rows_i_ != "</tr":
        rows[i] = 'X'
rows.remove('X')
print(rows)
l = ['a',"b",'c','d']
l.remove('b')
print(l)



