# Q1: Personal Bio Card
# This program displays student details in a formatted box.

# Using variables to store student information
student_name = "Amulya Grace Daki"
student_age = 20
student_course = "Python Programming"
student_college = "CMRIT"
student_email = "amulya@example.com"

# Display formatted card
print("╔══════════════════════════════════════╗")
print("║           STUDENT BIO CARD          ║")
print("╠══════════════════════════════════════╣")
print(f"║ Name    : {student_name:<25}║")
print(f"║ Age     : {student_age} years{'':<18}║")
print(f"║ Course  : {student_course:<25}║")
print(f"║ College : {student_college:<25}║")
print(f"║ Email   : {student_email:<25}║")
print("╚══════════════════════════════════════╝")