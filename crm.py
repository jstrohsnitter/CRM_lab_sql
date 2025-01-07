import psycopg2

connection = psycopg2.connect(database='crm_database')

cursor = connection.cursor()

def greet():
    greeting_input = input("What would you like to do?\n"
                           "Add employee? Enter 'Add Employee'. \n"
                           "Add Company? Enter 'Add Company'. \n"
                           "Find Employee? Enter 'Find Employee'. \n"
                           "Find Company? Enter 'Find Company'. \n"
                           "See all employees? Enter 'See all employees'. \n"
                           "See all companies? Enter 'See all companies'. \n"
                           "Update an employee? Enter 'Update employee'. \n"
                           "Update a company? Enter 'Update company'. \n"
                           "Delete an employee? Enter 'Delete employee'. \n"
                           "Delete a company? Enter 'Delete company'. \n"
                           "Exit app? Type CTRL + C (for mac or linux) or CRTL + Z (for windows) \n")
#------------------CREATE------------------------------------------------------
    if greeting_input == 'Add Employee':
        def create_employee():
            employee_input = input("Enter employee name ")
            cursor.execute('INSERT INTO employees (name) VALUES (%s)', [employee_input])
        create_employee()
        print("\n")
        greet()

    
    elif greeting_input == 'Add Company':
        def create_company():
            company_input = input("Enter company name ")
            cursor.execute('INSERT INTO companies (name) VALUES (%s)', [company_input])
        create_company()
        print("\n")
        greet()

#----------------READ-----------------------------------------------------------

    elif greeting_input == 'Find Employee':
        def find_employee():
            employee_search_input = input("Enter name of employee you want to find ")
            cursor.execute('SELECT * FROM employees WHERE name = (%s)', [employee_search_input])
            results = cursor.fetchall()
            print(results)
        find_employee()
        print("\n")
        greet()

    elif greeting_input == 'Find Company':
        def find_company():
            company_search_input = input("Enter name of company you want to find ")
            cursor.execute('SELECT * FROM companies WHERE name = (%s)', [company_search_input])
            results = cursor.fetchall()
            print(results)
        find_company()
        print("\n")
        greet()

    elif greeting_input == 'See all employees':
        def all_employees():
            cursor.execute('SELECT * FROM employees')
            results = cursor.fetchall()
            print(results)
        all_employees()
        print("\n")
        greet()

    elif greeting_input == 'See all companies':
        def all_companies():
            cursor.execute('SELECT * FROM companies')
            results = cursor.fetchall()
            print(results)
        all_companies()
        print("\n")
        greet()

#---------------------UPDATE----------------------------------------------
    elif greeting_input == 'Update employee':
        def update_employee():
            employee_search_input = input("Enter name of employee you want to update ")
            cursor.execute('SELECT * FROM employees WHERE name = (%s)', [employee_search_input])
            results = cursor.fetchall()
            print(results)
            update_info = input('Enter info you would like to update. If name, type name. If employer_id, type employer_id ')
            if update_info == 'name':
                new_name = input('Enter the new name ')
                cursor.execute('UPDATE employees SET name = (%s) WHERE name = (%s)', [new_name, employee_search_input])
            elif update_info == 'employer_id':
                new_employer_id = input('Enter the new employer_id ')
                cursor.execute('UPDATE employees SET employer_id = (%s) WHERE name = (%s)', [new_employer_id, employee_search_input])           
        update_employee()
        print("\n")
        greet()

    elif greeting_input == 'Update company':
        def update_company():
            company_search_input = input("Enter name of company you want to update ")
            cursor.execute('SELECT * FROM companies WHERE name = (%s)', [company_search_input])
            results = cursor.fetchall()
            print(results)
            update_company_name = input('Enter the new name of the company ')
            cursor.execute('UPDATE companies SET name = (%s) WHERE name = (%s)', [update_company_name, company_search_input])          
        update_company()
        print("\n")
        greet()

#---------------DELETE---------------------------------------------------
    elif greeting_input == "Delete employee":
        def delete_employee():
            employee_search_input = input("Enter name of employee you want to delete ")
            cursor.execute("DELETE FROM employees WHERE name = %s", [employee_search_input])
        delete_employee()
        print("Employee deleted.")
        print("\n")
        greet()

    elif greeting_input == "Delete company":
        def delete_company():
            company_search_input = input("Enter the name of the company you want to delete ")
            cursor.execute("DELETE FROM companies WHERE name = %s", [company_search_input])
        delete_company()
        print("Company deleted.")
        print("\n")
        greet()

# #---------------EXIT
#     elif greeting_input == "Exit":
#         def exit():
#             print("Exiting app.")
#             while True:
#                 user_input = input("Enter Exit. ")


greet()

connection.commit()

connection.close()



