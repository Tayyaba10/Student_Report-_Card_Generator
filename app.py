def grade_calculate(percentage):
    """Calculate the grade based on percentage."""
    if percentage >= 80:
        return 'A+'
    elif percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'Fail'

def display_report(student):
    print("\n===== STUDENT REPORT CARD =====")
    print(f"Name: {student['name']}")
    print(f"Roll Number: {student['roll_number']}")
    print("----------------------------")
    print("\nSubject-wise Marks:")

    total_marks = 0
    for subject, mark in student['marks'].items():
        print(f"{subject}: {mark} ({grade_calculate(mark)})")
        total_marks += mark
    print("\n")

    # Calculate percentage
    percentage = total_marks / len(student['marks'])
    final_grade = grade_calculate(percentage)

    print("-"*40)
    print(f"{'Total Marks:':<15}{total_marks:<10.1f}")
    print(f"{'Percentage:':<15}{percentage:<10.1f}%")
    print(f"{'Final Grade:':<15}{final_grade}")
    print("="*40)

def student_data():
   """Collect data for a single student."""
   name = input('Enter Student Name :')
   roll_number = input('Enter Student Roll Number :')
   subjects = ['Computer','English','Math','Physics','Urdu']
   marks = {}

   for subject in subjects:
       while True:
           try:
               mark = float(input(f"Enter your marks for {subject}: "))
               if 0 <= mark <= 100:
                   marks[subject] = mark
                   break
               else:
                   print("Marks should be between 0 and 100. Please enter again.")
           except ValueError:
                   print("Invalid input. Please enter a valid number.")
   # Create a dictionary to store student data
   student = {
        'name': name,
        'roll_number': roll_number,
        'marks': marks
    }
        
   return student

def main():
    students = []
    
    print("\n===== STUDENT REPORT CARD GENERATOR =====\n")

    while True:
        student = student_data()
        students.append(student)
        print(f"Record of {student['name']} inserted sucessfully.")

        choice = input("Do you want to add another student? (yes/no): ")
        if choice.lower() == 'no':
            break
         
    for student in students:
        display_report(student)
        
    print("\nThank you for using the Student Report Card Generator!")

if __name__ == "__main__":
    main()