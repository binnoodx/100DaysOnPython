class Employee:
    company = "Apple"
    def showDetails(self):
        print(f"{self.name} works in {self.company}")

    @classmethod
    #Taking class as argument
    def changeCompany(cls , newCompany):
        cls.company = newCompany

emp1 = Employee()
emp1.name = "Binod"
emp1.showDetails()

#Change default CompanyName variable for others too
emp1.changeCompany("Tesla")
emp1.showDetails()

emp2 = Employee()
emp2.name = "Harry"
emp2.showDetails()

