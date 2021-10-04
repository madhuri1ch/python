nums=[-1,-5,3,4]

print(sorted(nums)) #[-5, -1, 3, 4]

print(sorted(nums,key=abs)) #[-1, 3, 4, -5]

# key takes the function that is applied on each of the items and sorts on return value


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __repr__(self) -> str:
        return '({},{},{})'.format(self.name,self.age,self.salary)
    
e1=Employee('m',21,100)
e2=Employee('a',20,300)
e3=Employee('d',22,200)

employees=[e1,e2,e3]

print(e1) #(m,20,100) 
print(employees) #[(m,20,100), (a,21,200), (d,22,200)]

def emp_s(emp):
    return emp.age

print(sorted(employees,key=emp_s)) #[(a,20,300), (m,21,100), (d,22,200)]

print(sorted(employees,key=lambda e:e.salary)) #[(m,21,100), (d,22,200), (a,20,300)]


from operator import attrgetter

print(sorted(employees,key=attrgetter('name'))) #[(a,20,300), (d,22,200), (m,21,100)]