#Simulador de cajero automatico hecho por DIETMAR
import os

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print("Su saldo actual es: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposito aceptado. Saldo actual: ", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondo insuficiente!")
        else:
            self.balance -= amount
            print("Retiro aceptado. Saldo actual: ", self.balance)

atm = ATM()

username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")


if username == "Dietmar" and password == "12345678":
    while True:
        print("1. Verificar saldo")
        print("2. Deposito")
        print("3. Retiro")
        print("4. Salir")
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            atm.check_balance()
        elif opcion == "2":
            monto = int(input("Ingrese el monto a depositar: "))
            atm.deposit(monto)
        elif opcion == "3":
            monto = int(input("Ingrese el 4monto a retirar: "))
            atm.withdraw(monto)
        elif opcion == "4":
            break
        else:
            print("Opcion invalida!")

        os.system('clear')  
else:
    print("Credenciales invalidas!")
