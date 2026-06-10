# Historial
# La calculadora utiliza un historial temporal en memoria. Mientras la aplicación está en ejecución, 
# los datos ingresados por el usuario se almacenan en el campo de entrada para ser procesados. 
# Sin embargo, el proyecto no cuenta con una persistencia permanente de datos, por lo que las operaciones se eliminan al cerrar el programa. 
# Como mejora futura, se podría implementar un historial de operaciones almacenado en una lista, archivo de texto o base de datos.

# La calculadora maneja un historial temporal de datos mediante el campo de entrada (Entry). Cada vez que el usuario presiona un botón, el valor se almacena 
# momentáneamente en memoria y se muestra en pantalla.

# ¿Cómo funciona?
# 1.-El usuario presiona números y operadores.
# 2.-La función agregar_numero() inserta esos valores en el campo de entrada.
# 3.-La función realizar_operaciones() toma la expresión completa y la evalúa.
# 4.-El resultado reemplaza la operación escrita anteriormente.
# 5.-La función limpiar() elimina el contenido mostrado.

#Limitación del historial

# Actualmente la calculadora no guarda un historial permanente de las operaciones realizadas. Una vez que se realiza un nuevo cálculo o se cierra la aplicación, 
# las operaciones anteriores se pierden.