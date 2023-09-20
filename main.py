def newton_sqrt(n):
    x = 1  # Inicializa x en 1
    for k in range(9):  # Realiza exactamente 9 iteraciones
        x = (x + n / x) / 2
    return x, k + 1

# Pedir el valor de n al usuario
n = float(input("Ingrese el valor de n para calcular su raíz cuadrada: "))

x, k = newton_sqrt(n)
print(f"La raíz después de {k} iteraciones es {x}")
