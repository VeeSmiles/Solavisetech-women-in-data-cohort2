# student grade percentage + calculate percentage score

# Step 1: Get number of subjects
num_subjects = int(input("Please enter the number of subjects: "))

# Step 2: Create a list to store marks
marks = []
total_marks = 0

# Step 3: Get marks for each subject
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1} (out of 100): "))
    marks.append(mark)
    total_marks += mark

# Step 4: Calculate percentage
percentage = (total_marks / (num_subjects * 100)) * 100

# Step 5: Determine grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Step 6: Display results
print("\n--- Results ---")
print(f"Total Marks: {total_marks}/{num_subjects * 100}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")