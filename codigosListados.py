def round_to_two_decimal_places(n):
    # Round the number to 2 decimal places
    return round(n, 2)

# Get user input for the number
number = float(input("Ingrese el número a redondear: "))

# Round the number to two decimal places
rounded_number = round_to_two_decimal_places(number)

# Print the result
print(f"Número redondeado a dos decimales: {rounded_number}")
