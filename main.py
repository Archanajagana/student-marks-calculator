print("STUDENT MARKS CALCULATOR")
print("-----------------------")
name = input("Enter student name: ")
maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))
total = maths + python + english
average = total / 3
print("\n------ STUDENT RESULT ------")
print("Name:", name)
print("Total:", total)
print("Average:", round(average, 2))
if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
