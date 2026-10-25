marks = []

mark = int(input(" Enter mark (or -1 to stop): "))

while mark != -1:
    marks.append(mark)
    mark = int(input(" Enter mark (or -1 to stop): "))
    
print(f"Our List has {len(marks)} elements")

for x in range(len(marks)):
    print(f"Mark {x+1} is {marks[x]}")
    
sum = 0
for x in range(len(marks)):
    mark = marks[x]
    sum = sum + mark
    
print(f"The sum of all the marks = {sum}")

total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + mark
    
avg = total / len(marks)
print(f"The average of all marks = {avg}")