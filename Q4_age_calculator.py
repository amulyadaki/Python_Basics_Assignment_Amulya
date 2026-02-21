# Q4 - Age Calculator
# Calculates age in different units

from datetime import datetime

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = datetime.now().year

        if birth_year > current_year:
            print("Birth year cannot be in the future.")
            return

        current_age = current_year - birth_year
        age_in_months = current_age * 12
        age_in_days = current_age * 365
        age_in_hours = age_in_days * 24
        age_in_minutes = age_in_hours * 60
        years_until_100 = 100 - current_age

        print("\n=== AGE DETAILS ===")
        print("Current age:", current_age)
        print("Age in months:", age_in_months)
        print("Age in days:", age_in_days)
        print("Age in hours:", age_in_hours)
        print("Age in minutes:", age_in_minutes)
        print("Years until 100:", years_until_100)

    except ValueError:
        print("Invalid input! Enter numeric year.")
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()