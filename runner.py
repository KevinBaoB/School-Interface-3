from classes.school import School 
from classes.student import Student

school = School('Ridgemont High') 

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
        print(school.students)
    elif mode == '2':
        student_id = input('Enter student id:')
        student_string = str(school.find_student_by_id(student_id))
        print(student_string)
    elif mode == '3':
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
    
        school.add_student(Student(**student_data))

    elif mode == "4":
        student_to_remove = input('Enter student school ID:\n')

        school.remove_student(student_to_remove)
    
    elif mode == '5':
        break
