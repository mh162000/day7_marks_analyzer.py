# Part 1: Take input
marks = []

for i in range(5):
    num = int(input("Enter marks: "))
    marks.append(num)

# Part 2: Process data (AFTER loop)
print("All marks:", marks)

avg = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average:", avg)
print("Highest:", highest)
print("Lowest:", lowest)
