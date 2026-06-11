# Hola mi nombre es Kevin Leonardo Guzmán Gurrola y este es mi Proyecto final, que formara parte
# de mi calificación en las materias de "Introducción a la programación en software" 
# y "Laboratorio a la programación en software"

import tkinter as tk

# Función para agregar el número o operador al campo de entrada
def agregar_numero(numero):
    entrada.insert(tk.END, numero)

# Funcuión para realizar las operaciones aritmeticas básicas (+, -, * y /)
def realizar_operaciones():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Función para limpiar el campo de entrada
def limpiar():
    entrada.delete(0, tk.END)

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Realizar el campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Lista de botones con sus respectivos valores y la ubicación en la cuadrícula
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3)
]

# Ahora los botones y ubicamos la cuadrícula
for valor, fila, columna in botones:
    boton = tk.Button(
        ventana,
        text=valor,
        font=("Arial", 20),
        command=lambda v=valor: agregar_numero(v)
    )
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

# Creación de el botón para limpiar el campo de entrada
limpiar_boton = tk.Button(
    ventana,
    text="C",
    font=("Arial", 20),
    command=limpiar
)
limpiar_boton.grid(row=5, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")

# Creación de el botón para obtener el resultado
calcular_boton = tk.Button(
    ventana,
    text="=",
    font=("Arial", 20),
    command=realizar_operaciones
)
calcular_boton.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="nsew")

# Iniciamos el bucle principal de la aplicación
ventana.mainloop()
