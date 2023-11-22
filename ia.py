import tensorflow as tf

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la suma usando TensorFlow
suma_resultado = tf.add(num1, num2).numpy()

# Imprimir el resultado de la suma
print(f"La suma de {num1} y {num2} es: {suma_resultado}")

