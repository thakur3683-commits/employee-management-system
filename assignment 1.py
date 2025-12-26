employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000}
}


def add_egitmployee():
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id not in employees:
            break
        print("Employee ID already exists. Try again.")

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    print("Employee added successfully.")


def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 45)
    for emp_id, data in employees.items():
        print(emp_id, data["name"], data["age"],
              data["department"], data["salary"], sep="\t")


def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        emp = employees[emp_id]
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("Department:", emp["department"])
        print("Salary:", emp["salary"])
    else:
        print("Employee not found.")


def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using EMS.")
            break
        else:
            print("Invalid choice. Try again.")


main_menu()
