#Student mark analyzer
marks = []
for i in range (5):
    num = int(input("Enter marks:"))
    marks.append(num)
    for m in marks:
        print("all marks",marks)

        avg = sum(marks) / len(marks)
        m =max(marks)
        mi =min(marks)

print ("Average",avg)
print ("Highest",m)
print ("Lowest",mi)