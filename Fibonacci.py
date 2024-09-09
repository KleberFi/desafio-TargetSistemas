def is_fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    
    return a == n


numero = int(input("Informe um numero: "))


if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# A função is_fibonacci calcula a sequência de Fibonacci até que o número seja maior ou igual ao número fornecido. Se o número for encontrado, retorna True, caso não, retorna False.