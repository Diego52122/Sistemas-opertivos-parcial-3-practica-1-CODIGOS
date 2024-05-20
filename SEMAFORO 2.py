import threading
import time

# Semáforo binario para acceder a la base de datos
db_semaphore = threading.Semaphore(1)

# Simulación de una base de datos
class BancoDB:
    def __init__(self):
        self.balance = 1000  # Saldo inicial

    def consultar_balance(self):
        print(f"Balance actual: {self.balance}")

    def actualizar_balance(self, monto):
        print(f"Actualizando balance con: {monto}")
        self.balance += monto
        print(f"Nuevo balance: {self.balance}")

# Función que simula la operación de un cajero
def cajero(id, banco, monto):
    print(f"Cajero {id} intentando acceder a la base de datos")
    with db_semaphore:
        print(f"Cajero {id} ha adquirido el semáforo")
        banco.consultar_balance()
        banco.actualizar_balance(monto)
        print(f"Cajero {id} ha liberado el semáforo")
        time.sleep(1)  # Simulación del tiempo de operación del cajero

# Crear instancia de la base de datos
banco = BancoDB()

# Crear múltiples hilos que simulan los cajeros
cajeros = []
montos = [100, -50, 200, -30, 150]  # Monto de transacciones de cada cajero

for i in range(5):
    thread = threading.Thread(target=cajero, args=(i, banco, montos[i]))
    cajeros.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for cajero in cajeros:
    cajero.join()
