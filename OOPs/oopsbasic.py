# -*- coding: utf-8 -*-
"""
OOPS in Python
init method acts as a constructor
self is a referance to the instance of the class
class object attribute 'ethnicity remains true throughout'
"""

class Employee():
    #Class object attribute  remains true throughout
    ethnicity = 'Indian'
    
    def __init__(self,Salary,Working_hours):
        #Attribute
        #we take argument
        #we assign it using self.attributr name
        self.Salary=Salary
        #expect a int
        self.Working_hours=Working_hours
        
    #Actions the class object can perform
    #looks like functions
    
    def per_hour_wage(self):
        print("Per Hour Wage :")
        #referance the attribut es 
        print(self.Salary/self.Working_hours)

    
    
    
    
#new_emp=Employee()

new_emp1= Employee(600000, 40)   
new_emp2=Employee(400000, 32) 



type(new_emp1)

new_emp1.Salary
#returns salary
new_emp2.Working_hours

#to check object attribute ethnicity
#new_employee.(\tab) will give result for ethnicity

new_emp2.ethnicity
#calling method
new_emp1.per_hour_wage()
