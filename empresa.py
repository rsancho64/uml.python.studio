# inspirado en https://realpython.com/lessons/uml-diagrams/

# -------------------------------------------------------------------------------

# contadorEmpleados = 0  # BAD practise

class Employee:

    contadorEmpleados = 0  # BETTER: use: limited instances, singleton; ...

    def __init__(self, aName) -> None:
        self.name = aName

        # global contadorEmpleados
        # self.id = contadorEmpleados
        # contadorEmpleados += 1

        # BETTER:
        self.id = Employee.contadorEmpleados
        Employee.contadorEmpleados += 1

    def __str__(self) -> None:
        answ = ""
        answ += repr(self) + '\n\t'  # CAN TOGGLE THIS
        L = ["".join(it) for it in self.__dict__]
        answ += (str(L))
        return answ

# -------------------------------------------------------------------------------


class SalaryEmployee(Employee):

    def __init__(self, aName, aWage) -> None:
        super().__init__(aName)
        self.wage = aWage
        self.dias = 0

    def anotaDias(self, masDias):
        self.dias += masDias

    def calculate_payroll(self) -> int:
        pass

# -------------------------------------------------------------------------------


class ComissionEmployee(Employee):

    def __init__(self, aName, aComissionRate) -> None:
        super().__init__(aName)
        self.comissionRate = aComissionRate if aComissionRate < 100 else 10
        self.ventas = 0

    def anotaVentas(self, masVentas):
        self.ventas += masVentas

    def calculate_payroll(self) -> int:
        pass

# -------------------------------------------------------------------------------


class HourlyEmployee(Employee):

    def __init__(self, aName, aPayPerHour) -> None:
        super().__init__(aName)
        self.payPerHour = aPayPerHour if aPayPerHour < 80 else 50
        self.horas = 0

    def anotaHoras(self, masHoras):
        self.horas += masHoras

    def calculate_payroll(self) -> int:
        pass


# ===============================================================================


if __name__ == "__main__":

    e = Employee("ana")
    print(e)
    # print(repr(e), str(e))

    se = SalaryEmployee("mario", 1500)  # 1500 brutos/mes
    print(se)
    # print(repr(se), str(se))

    ce = ComissionEmployee("diego", 20)  # 20% de comiison de ventas
    print(ce)
    # print(repr(ce), str(ce))

    he = HourlyEmployee("juan", 60)  # 60 €/hora
    # print(repr(he), '\n\t', str(he))
    print(he)
