def gerar_lista(n):
    lista = []
    for i in range(1, n+1):
        asteriscos = '*' * i
        lista.append(asteriscos)

    return lista

# Exemplo prático: 
n = 5
resultado = gerar_lista(n)
print(resultado)      

  
