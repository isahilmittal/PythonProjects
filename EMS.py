#### emp = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Nisha', 'age': 25, 'department': 'IT', 'salary': 55000},
    104: {'name': 'Raj', 'age': 28, 'department': 'Marketing', 'salary': 52000},
    105: {'name': 'Priya', 'age': 26, 'department': 'Sales', 'salary': 48000}
}

def main_menu():
    EMS = True
    while EMS:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")
        
        try:
            x = int(input("Enter Menu Option: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
        
        if x == 1:
            add_employee()
        elif x == 2:
            view_employees()
        elif x == 3:
            search_employee()
        elif x == 4:
            print("Thank you for using our EMS")
            EMS = False
            exit()
        else:
            print("Please enter a valid option (1-4).")

def add_employee():
    print("\nAdd New Employee")

    # Get and validate Employee ID
    while True:
        try:
            emp_id = int(input("Enter Employee ID (numeric): "))
            if emp_id in emp:
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric Employee ID.")

    # Get Name
    name = input("Enter Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter Name: ").strip()

    # Get and validate Age
    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0:
                print("Age must be positive.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric Age.")

    department = input("Enter Department: ").strip()
    while not department:
        print("Department cannot be empty.")
        department = input("Enter Department: ").strip()

    while True:
        try:
            salary = float(input("Enter Salary: "))
            if salary < 0:
                print("Salary cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric Salary.")

    # Add to emp dictionary
    emp[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee {name} added successfully!")

        
    
def view_employees():
    if not emp:
        print("No employees available.")
        return
    
    print("-" * 65)
    print(f"{'ID':<6} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 65)
    
    for emp_id, details in emp.items():
        print(f"{emp_id:<6} {details['name']:<15} {details['age']:<5} {details['department']:<15} {details['salary']:<10}")
    print("-" * 65)

def search_employee():
    if not emp:
        print("No Employees Found.")
        return

    try:
        e = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid input! Please enter a numeric Employee ID.")
        return
    
    if e not in emp:
        print("Employee not found.")
    else:
        x = emp[e]
        print(f"Details for Employee ID {e}:")
        print(f"Name: {x['name']}")
        print(f"Age: {x['age']}")
        print(f"Department: {x['department']}")
        print(f"Salary: {x['salary']}")

main_menu()
