import datetime
import time

def hello_world(num_ejecuciones):
    try:
        for x in range(num_ejecuciones):
            now = datetime.datetime.now()
            print("Hello, World! La fecha es:", now)
            time.sleep(2)
    except ValueError as e:
        print("Error:", e)

# Solicitar al usuario el número de ejecuciones

try:
    num = int(input("Ingrese el número de ejecuciones: "))    
    hello_world(num)
except ValueError:
    print("Error: Por favor, ingrese un número válido.")
