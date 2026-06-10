# Interfaz Gráfica
# La interfaz gráfica de la Calculadora fue desarrollada utilizando Tkinter, la biblioteca estándar de Python para crear ventanas y aplicaciones visuales.

# Componentes principales:

# Ventana Principal
# ventana = tk.Tk()
# ventana.title("Calculadora")

# Esta ventana funciona como el contenedor principal de todos los elementos de la aplicación.

# Campo de Entrada
# entrada = tk.Entry(ventana, font=("Arial", 20), justify="right")

# Permite visualizar los números, operadores y resultados ingresados por el usuario. 
# El texto se muestra alineado a la derecha para asemejarse a una calculadora convencional.

# Botones
# La calculadora cuenta con botones numéricos del 0 al 9 y operadores matemáticos (+, -, *, /). Además incorpora:

# Botón C para limpiar la pantalla.
# Botón = para realizar los cálculos.

# Cada botón está asociado a una función que maneja su comportamiento al ser presionado, permitiendo contruir la expresión matemática que el usuario desea calcular.