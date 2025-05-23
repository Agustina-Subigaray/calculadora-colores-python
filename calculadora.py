import tkinter as tk

# Función que agrega números u operadores al visor
def click(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Configuración principal de la ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(bg="#1e1e2f")
ventana.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), bd=10, relief=tk.FLAT, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones (números y operadores)
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (texto, fila, col) in botones:
    if texto == "=":
        color = "#00c853"  # Verde
        comando = calcular
    elif texto in "+-*/":
        color = "#ff6d00"  # Naranja
        comando = lambda t=texto: click(t)
    else:
        color = "#3949ab"  # Azul
        comando = lambda t=texto: click(t)

    tk.Button(
        ventana, text=texto, font=("Arial", 16), width=5, height=2,
        bg=color, fg="white", command=comando, relief=tk.RAISED
    ).grid(row=fila, column=col, padx=5, pady=5)

# Botón de limpiar
tk.Button(
    ventana, text="C", font=("Arial", 16), width=22, height=2,
    bg="#d50000", fg="white", command=limpiar, relief=tk.RAISED
).grid(row=5, column=0, columnspan=4, padx=10, pady=10)

ventana.mainloop()
