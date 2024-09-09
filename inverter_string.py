def inverter_string(texto):
    string_invertida = ''
    for char in texto:
        string_invertida = char + string_invertida
    return string_invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")

# Ele percorre cada caractere da string original e o adiciona no início de uma nova string