# Q6 - Grade Calculator
# Calculates total marks, percentage, grade, and pass/fail result

def main():
    try:
        marks = []

        # Taking marks input for 5 subjects
        for subject_number in range(1, 6):
            subject_mark = float(input(f"Enter marks for subject {subject_number}: "))

            # Validate marks range
            if subject_mark < 0 or subject_mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(subject_mark)

        # Calculating total and percentage
        total_marks = sum(marks)
        percentage = total_marks / 5

        # Determining grade based on percentage
        if percentage >= 90:
            grade = "A+ (Outstanding)"
        elif percentage >= 80:
            grade = "A (Excellent)"
        elif percentage >= 70:
            grade = "B (Good)"
        elif percentage >= 60:
            grade = "C (Average)"
        elif percentage >= 50:
            grade = "D (Pass)"
        else:
            grade = "F (Fail)"

        # Checking pass/fail condition (all subjects must be >= 40)
        result = "Pass" if all(mark >= 40 for mark in marks) else "Fail"

        # Displaying results
        print("\n=== RESULT ===")
        print("Total Marks:", total_marks)
        print("Percentage:", percentage)
        print("Grade:", grade)
        print("Final Result:", result)

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()