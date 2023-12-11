# inspirado en https://realpython.com/lessons/uml-diagrams/

contadorEmpleados = 0

class Employee:

    def __init__(self, aName) -> None:
        global contadorEmpleados
        self.name = aName
        self.id = contadorEmpleados
        contadorEmpleados += 1

    def __str__(self) -> None:
        return (f"{self.id}:{self.name}")

class SalaryEmployee(Employee):
    
    def __init__(self, aName, aWage) -> None:
        super(aName) # ...

    def calculate_payroll(self) -> int


class ComissionEmployee(SalaryEmployee):
    pass

class HourlyEmployee(Employee):
    pass


if __name__ == "__main__":

    e = Employee("ana")
    print(repr(e), str(e))

    se = SalaryEmployee("mario")
    print(repr(se), str(se))

    ce = ComissionEmployee("andres")
    print(repr(ce), str(ce))

    he = HourlyEmployee("juan")
    print(repr(he), str(he))

