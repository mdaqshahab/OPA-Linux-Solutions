class Employee:
    def __init__(self,id,name,department,salary,role):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.role = role

class Organisations:
    def __init__(self,roleper,emp):
        self.roleIn = roleper
        self.emp  = emp

    def fetch(self, em):
        r = em.role
        if r in self.roleIn.keys():
            return self.roleIn[r]
        return None

    def calculate(self, d_name):
        l = []
        for em in self.emp:
            if em.department == d_name:
                a = self.fetch(em)
                if a != None:
                    inc = (em.salary * a)/100
                    em.salary = em.salary + inc
                    l.append(em)
        if len(l)>0:
            return l
        else:
            return None

if __name__ == '__main__':
    no_role = int(input())
    d = {}
    for i in range(no_role):
        r = input()
        incentive = int(input())
        d[r] = incentive
    l_emp = []
    no_emp = int(input())
    for i in range(no_emp):
        e_id = int(input())
        name = input()
        dep = input()
        sal = float(input())
        role = input()
        employee = Employee(e_id,name,dep.lower(),sal,role)
        l_emp.append(employee)
    department = input()
    org = Organisations(d,l_emp)
    in_per = org.fetch(l_emp[0])
    if in_per != None:
        print(in_per)
    else:
        print("Employee Not found")
    li = org.calculate(department.lower())
    if li != None:
        for i in li:
            print(i.id," ", i.name," ",i.salary)
    else:
        print("Employees Not found")


