temp_in_celsius = int(input("Enter the temp in celsius: "))
temp_in_fahrenheit = temp_in_celsius * (9 / 5) + 32
print("Temperature in Fahrenheit: ", temp_in_fahrenheit)

input_temp = int(input("Enter the temp in fahrenheit: "))
temp_in_c = (input_temp - 32) * 5/9
print("Temperature in Celsius: ", temp_in_c)