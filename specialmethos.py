class Emp:

    raiseamt=1.04
    no_of_emp=0
    def __init__(self,Fname,Lname,pay):
        self.Fname=Fname
        self.Lname=Lname
        self.pay = pay
        self.Email=Fname + '.' + '@company.com'

        Emp.no_of_emp +=1

    def Fullname(self):
        return '{} {}'.format(self.Fname,self.Lname)

    def apply_raise(self):
        self.pay=int(self.pay*self.raiseamt)

    def __repr__(self):
        return "Emp('{}','{}',{})".format(self.Fname,self.Lname,self.pay)


    def __str__(self):
        return '{} - {}'.format(self.Fullname(),self.Email)


emp1=Emp('Swapnil','Dhoble',50000)
emp2=Emp('Akash','Wadhawane',60000)
print(emp1)

print(repr(emp1))
print(str(emp1))

print()