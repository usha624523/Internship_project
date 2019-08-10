class Employee():
    'Common base class for all employees'
    

    def __init__(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
    
     
    def displayEmployee(self):
        print ("eid : ", self.eid,", Name : ", self.name,  ", Salary: ", self.salary)
    

emp1 = Employee(1,"Zara", 2000,10)

emp2 = Employee(2,"meera", 4000,20)
emp1.displayEmployee()
emp2.displayEmployee()
