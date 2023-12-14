# inspirado en: https://realpython.com/lessons/uml-diagrams/
# interfaces:   https://realpython.com/python-interface/#using-abcabcmeta
# -------------------------------------------------------------------------------

import abc

class Interface(metaclass=abc.ABCMeta):
    """interfase de pago para empleados diversos"""    

    @abc.abstractmethod
    def calculate_payroll(self):
        """pagar al trabajador"""
        raise NotImplementedError

class Employee:
    """superclase para empleados especificos"""
    contadorEmpleados = 0

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

    def calculate_payroll(self) -> float:
        cantidad = self.wage * self.dias / 30
        #print (f"soy un {self.__class__.__name__} y he cobrado {cantidad}")
        return cantidad

# -------------------------------------------------------------------------------


class ComissionEmployee(SalaryEmployee):

    def __init__(self, aName, aWage, aComissionRate = 10) -> None:
        super().__init__(aName, aWage)
        self.comissionRate = aComissionRate if aComissionRate < 100 else 10
        self.ventas = 0

    def anotaVentas(self, masVentas):
        self.ventas += masVentas

    def calculate_payroll(self) -> int:
        cantidad = super().calculate_payroll()
        cantidad += self.ventas * self.comissionRate / 100
        return cantidad
        

# -------------------------------------------------------------------------------


class HourlyEmployee(Employee):

    def __init__(self, aName, aPayPerHour) -> None:
        super().__init__(aName)
        self.payPerHour = aPayPerHour if aPayPerHour < 80 else 50
        self.horas = 0

    def anotaHoras(self, masHoras):
        self.horas += masHoras

    def calculate_payroll(self) -> int:
        cantidad = self.horas * self.payPerHour
        return cantidad


# ===============================================================================


if __name__ == "__main__":

    # e = Employee("ana")
    # print(e)

    se = SalaryEmployee("mario", 1500)  # 1500 brutos/mes
    print(se)
    print(se.calculate_payroll())
    se.anotaDias(15)
    print(se.calculate_payroll())

    ce = ComissionEmployee("diego", 1500, 20)  # 20% de comiison de ventas
    print(ce.calculate_payroll())
    ce.anotaDias(15)
    ce.anotaVentas(6000)
    print(ce.calculate_payroll())

    he = HourlyEmployee("juan", 60)  # 60 €/hora
    print(he.calculate_payroll())
    he.anotaHoras(10)
    print(he.calculate_payroll())

    
