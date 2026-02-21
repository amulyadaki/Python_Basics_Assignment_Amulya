# Q6 - Grade Calculator
# Calculates total, percentage, grade, and pass/fail

def main():
    try:
        marks = []
        for i in range(1, 6):
            subject_mark = float(input(f"Enter marks for subject {i}: "))
            if subject_mark < 0 or subject_mark > 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(subject_mark)

        total_marks = sum(marks)
        percentage = total_marks / 5

        # Grade determination
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

        result = "Pass" if all(mark >= 40 for mark in marks) else "Fail"

        print("\n=== RESULT ===")
        print("Total:", total_marks)
        print("Percentage:", percentage)
        print("Grade:", grade)
        print("Final Result:", result)

    except ValueError:
        print("Invalid input! Enter numeric marks.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()