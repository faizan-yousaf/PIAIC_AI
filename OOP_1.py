#In this file I'll try to cover the basics of Class and Objects:
# We will work on 2 classes : 1= Employee 2= Student

# class Employee():
#     pass

# emp_1 = Employee()
# emp_2 = Employee()
# if we run this code, it will execute successfully!


#Creating Employee Class
class Employee():

    #constructor method
    def __init__(self, first, last, department, pay): 
        #attributes
        self.fName = first  
        self.lName = last  
        self.pay = pay
        self.department = department
        self.Email = first + "." + last + "@gmail.com"
        self.fullName = first + " " + last

    def displayEmployeeInfo(self): #method
        return f"The employee name is {self.fName} {self.lName}, a part of {self.department} department and taking sallery of {self.pay} Dollars."

    
# Let's make Instances
emp1 = Employee("Muhammad", "Faizan", "CS", "50000" )
emp2 = Employee("hamza", "ashraf", "IT", "60000")

print(emp1.displayEmployeeInfo())
print(emp2.displayEmployeeInfo())
print(emp2.Email)
print(emp2.fullName)

