# Program demonstrating attributes and behaviors of classes and objects
print('____________________classes_and_objects.py_____________________')


# Definition of Employee class
class Employee:
    # Class-level variable shared by all objects of the class.
    # Can be accessed using class name (i.e. Employee.employee_count)
    input("\n  [In class Employee]")
    input("  Class-level variable shared by ALL objects of the class.")
    input("  Can be accessed using class name (i.e. Employee.employee_count)")
    input("  []> employee_count = 0")
    employee_count = 0

    # __init__ called AUTOMATICALLY when an object is created
    def __init__(self, name, job_title):
        input("\n  [In class Employee]")
        input("  __init__ called AUTOMATICALLY when an object is created")
        input("  []> def __init__(self, name, job_title):")

        input("  Assigning argument 'name' to instance variable 'self.name'")
        input("  []>     self.name = name")
        # Assign argument 'name' to instance variable 'self.name'
        self.name = name

        input("  Assign argument 'job_title' to instance variable 'self.__job_title'")
        input("  Variables with '__' are only visible to members of the class")
        input("  This WILL make the __job_title variable PRIVATE in Class")
        input("  []>     self.__job_title = job_title")
        # Assign argument 'job_title' to instance variable 'self.__job_title'
        # Variables with '__' are only visible to members of the class
        # This will make __job_title private
        self.__job_title = job_title

        input("  Incrementing the class-level variable employee_count")
        input("  []>     Employee.employee_count += 1")
        # increment the class-level variable employee_count
        Employee.employee_count += 1

    # Get INSTANCE variables self.name and self.__job_title
    def get_employee(self):
        input("\n  [In class Employee]")
        input("  Getting INSTANCE variables self.name and self.__job_title")
        input("  []> def get_employee(self):")
        input("  []>     return self.name, self.__job_title")
        return self.name, self.__job_title

    # Set INSTANCE variables self.name and self.__job_title
    def set_employee(self, name, job_title):
        # Assign argument name to instance variable self.name
        self.name = name
        # Assign argument job_title to instance variable self.__job_title
        self.__job_title = job_title

    # Display CLASS-LEVEL variable employee_count
    def display_count(self):
        input("\n  [In class Employee]")
        input("  Displaying CLASS-LEVEL variable employee_count")
        input("  []> display_count(self)")
        input('  []>     print("Total Employee(s): {}".format(Employee.employee_count))')

        print("Total Employee(s): {}".format(Employee.employee_count))

    # Display INSTANCE variable self.__job_title
    # Note: accessing the '__' variable here from within the class
    def display_employee(self):
        input("\n  [In class Employee]")
        input("  Displaying INSTANCE variable self.__job_title")
        input("  []> def display_employee(self):")
        input('  []>     print("Name:", self.name, "--- Job Title:", self.__job_title)')

        print("Name:", self.name, "--- Job Title:", self.__job_title)


# main() function
def main():
    input('\n ############### Employee 1 ###############')

    input('\nInstantiating employee_1 from Employee class,'
          '\nemployee_1 is now an Employee object')
    input('> employee_1 = Employee("Fredricka", "The Big Boss")')
    # instance employee_1 object from Employee class
    employee_1 = Employee("Fredricka", "The Big Boss")

    input('\nCalling the display_employee() method of employee_1:')
    input('> employee_1.display_employee()')
    # Call the display_employee() method of employee_1
    employee_1.display_employee()

    input('\nCalling the display_count() method of employee_1')
    input('> employee_1.display_count()')
    # Call the display_count() method of employee_1
    employee_1.display_count()

    input('\nAccessing INSTANCE variable self.name, so a variable'
          '\nINSIDE methods of the class Employee:')
    input('> USING .format(employee_1.name)')
    # Access INSTANCE variable self.name
    input('employee_1.name: {}\n'.format(employee_1.name))

    print('\n\n ############### Employee 2 ###############')

    input('\nInstantiating employee_2 from Employee class,'
          '\nemployee_2 is now an Employee object')
    input('> employee_2 = Employee("Cierra", "The Little Boss")')
    # instance employee_2 object from Employee class
    employee_2 = Employee("Cierra", "The Little Boss")

    input('\nCalling the display_employee() method of employee_2:')
    input('> employee_2.display_employee()')
    # Call the display_employee() method of employee_2
    employee_2.display_employee()

    input('\nCalling the display_count() method of employee_2')
    input('> employee_2.display_count()')
    # Call the display_count() method of employee_2
    employee_2.display_count()

    input('\nAccessing INSTANCE variable self.name, so a variable'
          '\nINSIDE methods of the class Employee:')
    input('> USING .format(employee_2.name)')
    # Access INSTANCE variable self.name
    print('employee_1.name: {}\n'.format(employee_2.name))

    input("\nAccessing CLASS-LEVEL variable employee_count from the Employee class")
    input('> USING .format(Employee.employee_count)')
    # Access CLASS-LEVEL variable employee_count from Employee class
    print("Total Employee(s): {}".format(Employee.employee_count))

    input("\nAttempting to access an instance variable with double underscore '__' prefix"
          "\nOUTSIDE of its class will generate an error")
    input("> print(employee_1.__job_title)")
    # Attempting to access an instance variable with double underscore "__" prefix
    # OUTSIDE of its class will generate an error
    # print(employee_1.__job_title)

if __name__ == '__main__':
    main()

else:
    pass
