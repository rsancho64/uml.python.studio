# inspirado en https://realpython.com/lessons/uml-diagrams/

contadorEmpleados = 0

class Employee:

    def __init__(self, aName) -> None:
        self.name = aName
        self.id = aName # contadorEmpleados
        # contadorEmpleados += 1

    def __str__(self) -> None:
        return (f"{self.id}:{self.name}")

class SalaryEmployee(Employee):
    pass


class HourlyEmployee(Employee):
    pass


if __name__ == "__main__":

    e = Employee("ana")
    print(repr(e), str(e))

    se = SalaryEmployee("mario")
    print(repr(se), str(se))

    he = HourlyEmployee("juan")
    print(repr(he), str(he))

