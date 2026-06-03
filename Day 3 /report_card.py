def user_input():
    name = input("Enter the student's name: ")
    roll_number = input("Enter the student's roll number: ")
    marks = {
        'Math': float(input("Enter marks for Math: ")),
        'Science': float(input("Enter marks for Science: ")),
        'Computer': float(input("Enter marks for English: ")),
    }
    return {
        'name': name,
        'roll_number': roll_number,
        'marks': marks
    }

def calculate_percentage(marks):
    total_marks = sum(marks.values())
    percentage = (total_marks/ (len(marks) * 100)) * 100
    return percentage

def pass_fail_status(marks):
    for mark in marks.values():
        if mark < 40:
            return 'Fail'
    return 'Pass'

def grading_system(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
    

def distinction_reward(percentage):
    if percentage >= 90:
        return 'Distinction | Great Work!'
    else:
        return "Satisfactory" if percentage >= 60 else "Needs Improvement"
    

def report_card():
    # Take the user input for student details and marks
    student_info = user_input()

    # Calculate the percentage
    percentage = calculate_percentage(student_info['marks'])
    
    # Determine pass/fail status
    status = pass_fail_status(student_info['marks'])

    # Determine the grade
    grade = grading_system(percentage)

    # Determine distinction
    distinction = distinction_reward(percentage)

    # Printing the report card
    single_line = "-" * 60
    double_line = "=" * 60

    print(double_line)
    print("")
    print(f"                Student's Report Card")
    print("")
    print(double_line)
    print(f"Name: {student_info['name'].capitalize()}       |        Roll Number: {student_info['roll_number']}")
    print(single_line)
    for subject, mark in student_info['marks'].items():
        print(f"{subject:<24} : {mark}")
    print(single_line)
    print(f"Percentage: {percentage:.2f}% | Status: {status} | Grade: {grade}")
    print(single_line)
    print(f"Remarks: {distinction}")
    print(double_line)


report_card()

