
decimal_num = 45.5455
whole_num = int(decimal_num)
print(f'Type of whole_num is {type(whole_num)} and value is {whole_num}')

string_1 = " 45231 "
string_1_integer = int(string_1)
print(f'Type after conversion is {type(string_1_integer)}')

whole_num_2 = 123
whole_num_2_float = float(whole_num_2)
print(f'Type after conversion is {type(whole_num_2_float)}')
print(f'Value of whole_num_2_float is {whole_num_2_float}')

string_2 = "98.76"
string_2_float = float(string_2)
print(f'Type after conversion is {type(string_2_float)}')
print(f'Value of string_2_float is {string_2_float}')

print(str(whole_num_2) + str(124) + str(["Kasia", "Arek", "Marek"]) + str(123.321))
print(whole_num_2, 123, {"Kasia", "Arek", "Marek"})