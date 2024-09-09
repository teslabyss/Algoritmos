"""
Programa que calcula la edad de un perro y un gato en años humanos
"""
# Calcula la edad del perro y el gato en años humanos
def calculate_ages(humanYears):
    # Operación de años gato
    if humanYears == 1:
        catYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
    else:
        catYears = 15 + 9 + 4 * (humanYears - 2)

    # Operación de años perro
    if humanYears == 1:
        dogYears = 15
    elif humanYears == 2:
        dogYears = 15 + 9
    else:
        dogYears = 15 + 9 + 5 * (humanYears - 2)

    # Devuelve los resultados
    return [humanYears, catYears, dogYears]

# Solicita al usuario que ingrese los años humanos
human_years = int(input("Ingresa el número de años humanos: "))

# Calcula las edades correspondientes
ages = calculate_ages(human_years)

# Imprime los resultados
print(f"Los años en humanos son: {ages[0]}")
print(f"Los años del gato son: {ages[1]}")
print(f"Los años del perro son: {ages[2]}")

