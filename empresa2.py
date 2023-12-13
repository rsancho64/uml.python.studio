# inspirado en: https://realpython.com/lessons/uml-diagrams/
# interfaces:   https://realpython.com/python-interface/#using-abcabcmeta
# -------------------------------------------------------------------------------

# contadorEmpleados = 0  # BAD practise

class Employee:
    """superclase para empleados especificos"""
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
        # answ += repr(self) + '\n\t'  # CAN TOGGLE THIS
        answ += str(vars(self))
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


class ComissionEmployee(SalaryEmployee):

    def __init__(self, aName, aWage, aComissionRate = 10) -> None:
        super().__init__(aName, aWage)
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

    se = SalaryEmployee("mario", 1500)  # 1500 brutos/mes
    print(se)

    ce = ComissionEmployee("diego", 1500, 20)  # 20% de comiison de ventas
    print(ce)

    he = HourlyEmployee("juan", 60)  # 60 €/hora
    print(he)
