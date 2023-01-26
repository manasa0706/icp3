class Employee:
    count = 0
    salary_amt = 0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1
        Employee.salary_amt = Employee.salary_amt + salary

    def average_salary(self):
        return Employee.salary_cnt/Employee.count


class FulltimeEmployee(Employee):
    pass

fulltime_employee1 = FulltimeEmployee("Ram", "krishna", 12000, "Business Analyst")
fulltime_employee2 = FulltimeEmployee("Micheal", "Jordan", 10000, "Clerk")
print(fulltime_employee2.average_salary())
employee1 = Employee("Bob", "Joe", 6000, "Network Engineer")
employee2 = Employee("Ricky", "Thomas", 8000, "Network Engineer")
print(employee1.average_salary())
