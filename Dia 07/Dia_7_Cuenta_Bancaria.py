class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.num_cuenta}\nBalance: {self.balance}"

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto > self.balance:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            self.balance -= monto


def crear_cliente():
    nombre = input("Ingresa el nombre del cliente: ")
    apellido = input("Ingresa el apellido del cliente: ")
    num_cuenta = input("Ingresa el número de cuenta del cliente: ")
    balance = float(input("Ingresa el balance inicial de la cuenta: "))
    return Cliente(nombre, apellido, num_cuenta, balance)


def inicio():
    cliente = crear_cliente()
    while True:
        print(cliente)
        accion = input("¿Quieres depositar (D), retirar (R) o salir (S)? ").upper()
        if accion == "D":
            monto = float(input("Ingresa el monto a depositar: "))
            cliente.depositar(monto)
        elif accion == "R":
            monto = float(input("Ingresa el monto a retirar: "))
            cliente.retirar(monto)
        elif accion == "S":
            print("Gracias por usar nuestro servicio.")
            break
        else:
            print("Acción no válida.")

inicio()


