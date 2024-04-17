#area de un cuadrado

lado = float(input("Por favor diga la longitud del lado en cm: "))
area = lado ** 2

print(f"El área del cuadrado con lado {lado}, es de {area} cm.")

#perimetro del cuadrado
perimetro = lado * 4

print(f"El perímetro del cuadrado con lado {lado}, es de {perimetro} cm.")

#hacer que funcione en una funcion con o sin parametros

def calcular_area_cuadrado(lado):
    if lado <= 0:
        raise ValueError("El lado del cuadrado debe ser un número positivo.")
    return lado ** 2

def calcular_perimetro_cuadrado(lado):
    if lado <= 0:
        raise ValueError("El lado del cuadrado debe ser un número positivo.")
    return lado * 4

# Ejemplo de uso sin parámetros
lado = 5
area = calcular_area_cuadrado(lado)
perimetro = calcular_perimetro_cuadrado(lado)

print(f"El área del cuadrado con lado {lado} cm es de {area} cm^2.")
print(f"El perímetro del cuadrado con lado {lado} cm es de {perimetro} cm.")

# Ejemplo de uso con parámetros
lado_usuario = float(input("Ingrese la longitud del lado del cuadrado (en cm): "))
area_usuario = calcular_area_cuadrado(lado_usuario)
perimetro_usuario = calcular_perimetro_cuadrado(lado_usuario)

print(f"El área del cuadrado con lado {lado_usuario} cm es de {area_usuario} cm^2.")
print(f"El perímetro del cuadrado con lado {lado_usuario} cm es de {perimetro_usuario} cm.")

