print("Welcome to the Student Data Organizer!")
choice = None
students = []
ID = 0

while choice != 6:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = (input("Enter your choice: "))
    choice = int(choice)

    if(choice == 1):
        ID += 1
        print("\nEnter student details:")
        print("Student ID: {}".format(ID+100))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")
        s_name = name
        s_age = age
        s_grade = grade
        s_dob = tuple(dob.split("-"))
        s_subjects = set(subjects.split(","))
        print("\nStudent added successfully!")
        new_stud = {"Student ID" : ID,
                        "Name" : s_name,
                        "Age" : s_age,
                        "Grade" : s_grade,
                        "d.o.b." : s_dob,
                        "Subjects" : s_subjects}
        students.append(new_stud)
    elif(choice == 2):
        print("--- Display All Students ---")
        for i in range(ID):
            print(f"Student ID: {students[i]["Student ID"]+100} | Name: {students[i]["Name"]} | Age: {students[i]["Age"]} | Grade: {students[i]["Grade"]} | Subjects: {[k for k in students[i]['Subjects']]}")
    elif(choice == 3):
        update_id = int(input("Enter ID you want to update: "))
        while True:
            print("\nSelect what you want to update:")
            print("1. ID")
            print("2. Name")
            print("3. Age")
            print("4. Grade")
            print("5. D.O.B.")
            print("6. Subjects")
            print("7. Back to Menu")
            update_choice = int(input("Enter your choice:"))

            if(update_choice == 1):
                print("[Error: Can not update a tuple!]")
                continue
            elif(update_choice == 2):
                updated_name = input("Enter new name: ")
                students[(update_id-101)]["Name"] = updated_name
            elif(update_choice == 3):
                updated_age = int(input("Enter new age: "))
                students[(update_id-101)]["Age"] = updated_age
            elif(update_choice == 4):
                updated_grade = input("Enter new grade: ")
                students[(update_id-101)]["Grade"] = updated_grade
            elif(update_choice == 5):
                print("[Error: Can not update a tuple!]")
                continue
            elif(update_choice == 6):
                updated_subjects = input("Enter new subjects(comma-separated): ")
                students[(update_id-101)]["Subjects"] = set(updated_subjects.split(","))
            elif(update_choice == 7):
                break
            else:
                print("Invalid choice!")
                continue
    elif(choice == 4):
        del_student = int(input("\nEnter Student ID to delete: "))
        print("Student at ID: %d" % del_student)
        print(f"Student ID: {del_student} | Name: {students[del_student-101]["Name"]} | Age: {students[del_student-101]["Age"]} | Grade: {students[del_student-101]["Grade"]} | Subjects: {[k for k in students[del_student-101]['Subjects']]}")
        while True:
            print("Confirm to delete:")
            print("1. Yes")
            print("2. Cancle")
            del_choice = int(input("Enter your choice: "))
            if(del_choice == 1):                
                remove_stud = students[del_student-101]
                students.remove(remove_stud)
                ID -= 1
                print("Student removed successfully!")
                break
            elif(del_choice == 2):
                print("Student removal terminated")
                break
            else:
                print("Invalid choice!")
                continue
    elif(choice == 5):
        show_subjects = int(input("Enter student ID: "))
        print("Sbjects offered to student %d" %show_subjects)
        print(students[show_subjects-101]["Subjects"])
    elif(choice > 6):
        print("Invalid Option!")
        continue