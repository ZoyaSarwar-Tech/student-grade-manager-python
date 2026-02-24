student={}
while True:
    print("STUDENT GRADE MANAGEMENT SYSTEM")

    print("1.Add New Students")
    print("2.Add Marks")
    print("3.View Students Details")
    print("4.View Student List")
    print("5.Exit")
    choice=input("Enter your choice(1-5): ")
    if choice=="1":
        print("1. Add New Student")
        print("-"*50)
        name=input("Enter your student name: ")
        if name in student:
            print("Student Name Already Exist")
        else:
            student[name]={}
            print(f"student name: {name} has been added")
    elif choice=="2":
        print("2. Add Marks")
        print("-"*50)
        name=input("Enter your student name: ")
        if name not in student:
            print("Student Name Not Exist")
            continue
        subject=input("Enter subject: ")
        marks=float(input("Enter marks: "))
        if marks <0 or marks > 100:
            print("Marks add between 0-100")
            continue
        student[name][subject]=marks
        print(f"subject {subject} and marks {marks}has been added")
    elif choice=="3":
        print("3. View Student Details")
        print("-"*50)
        name=input("Enter your student name: ")
        if name not in student:
            print("Student Name Not Exist")
            continue
        print(f"{name} Record")
        total=0
        for subject,marks in student[name].items():
            print(f"subject: {subject} marks: {marks}")
            total+=marks
        if student[name]:
            average=total/len(student[name])
            print(f"average marks: {average:.2f}")
            if average>=90:
                print("Grade A")
            elif average>=80:
                print("Grade B")
            elif average>=70:
                print("Grade C")
            elif average>=60:
                print("Grade D")
            else:
                print("Grade E")

    elif choice=="4":
        print("4.View Student List")
        print("-"*50)

        if not student:
            print("There is no student ")
            continue
        else:
            print(" All Students List")
            for name in student:
                print(f"{name} : ({len(student[name])} students)")
    elif choice=="5":
        print("5.Exit")
        print("-"*50)
        print("Thank You")
        break
    else:
        print("Invalid Choice")



