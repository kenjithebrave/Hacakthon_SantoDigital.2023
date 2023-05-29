def menor_diferenca(array):
    array.sort()               # Coloquei essa função para ordenar a array em ordem crescente
    menor_dif = float('inf')   # Esta função irá definir uma diferença que é inicialmente infinita
    menores_pares = []         # Criei a lista para armazenar os numeros pares com a menor diferença entre si

    # Em seguida, preciso criar uma estrutura de repetição para percorrer a array e achar a menor diferença
    
    for i in range(len(array) - 1): # Defini como parâmetro que percorra o tamanho da array
        diferenca = abs(array[i] - array[i+1])
          
        if diferenca < menor_dif: 
            menor_dif = diferenca
            menores_pares = [(array[i], array[i+1])]
        elif diferenca == menor_dif:
            menores_pares.append((array[i], array[i+1]))
            
    return menores_pares

# Exemplo de uso:
array = [3, 8, 50, 5, 1, 18, 12]
menores_pares = menor_diferenca(array)
print(menores_pares)            

# A saída esperada deve ser: [(1, 3), (3, 5)], considerando que possuem as menores diferenças do conjunto do exemplo.
