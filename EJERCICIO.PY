# Ejercicio 1
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

# Ejercicio 2
contraseña_guardada = "contraseña"
contraseña_usuario = input("Introduce la contraseña: ")
if contraseña_usuario.lower() == contraseña_guardada.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

# Ejercicio 3
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num2 != 0:
    print(f"La división es: {num1 / num2}")
else:
    print("Error: No se puede dividir entre cero.")

# Ejercicio 4
numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 5
edad = int(input("¿Cuántos años tienes? "))
ingresos = float(input("¿Cuáles son tus ingresos mensuales? "))
if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")

# Ejercicio 6
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (mujer/hombre): ").lower()
if sexo == "mujer" and nombre.lower() < "m":
    print("Te corresponde el grupo A.")
elif sexo == "hombre" and nombre.lower() > "n":
    print("Te corresponde el grupo A.")
else:
    print("Te corresponde el grupo B.")

# Ejercicio 7
renta = float(input("Introduce tu renta anual: "))
if renta < 10000:
    print("Tipo impositivo: 5%")
elif renta < 20000:
    print("Tipo impositivo: 15%")
elif renta < 35000:
    print("Tipo impositivo: 20%")
elif renta < 60000:
    print("Tipo impositivo: 30%")
else:
    print("Tipo impositivo: 45%")

# Ejercicio 8
puntuacion = float(input("Introduce tu puntuación: "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 2400 * puntuacion
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion
else:
    nivel = "Puntuación no válida"
    dinero = 0

print(f"Nivel: {nivel}, Dinero: {dinero}€")

# Ejercicio 9
edad_cliente = int(input("¿Cuántos años tiene el cliente? "))
if edad_cliente < 4:
    print("Entrada gratuita.")
elif 4 <= edad_cliente <= 18:
    print("El precio de la entrada es 5€.")
else:
    print("El precio de la entrada es 10€.")

# Ejercicio 10
tipo_pizza = input("¿Quieres una pizza vegetariana? (sí/no): ").lower()
if tipo_pizza == "sí":
    ingredientes = ["Pimiento", "Tofu"]
    print("Ingredientes disponibles: Pimiento, Tofu")
else:
    ingredientes = ["Peperoni", "Jamón", "Salmón"]
    print("Ingredientes disponibles: Peperoni, Jamón, Salmón")

ingrediente = input(f"Elige un ingrediente (además de mozzarella y tomate): {ingredientes}: ")
if ingrediente in ingredientes:
    print(f"Pizza no vegetariana con: Mozzarella, Tomate y {ingrediente}")
else:
    print("Ingrediente no válido.")
