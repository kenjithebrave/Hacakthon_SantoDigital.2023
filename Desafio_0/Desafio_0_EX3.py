def subconjuntos(nums):
    result = [[]] # De início, defini o conjunto como vazio
    
    for num in nums:
        # Nesse laço de repetição, arranjei de forma que cada novo número seja adicionado 
        # aos subconjuntos existentes e crei novos que contenham apenas o número atual
        result += [subset + [num] for subset in result]
    
    """Na minha cabeça a estrutura devia funcionar 
    da seguinte forma: Ao chamar a função com uma entrada '[1, 2]', o subconjunto vazio '[]' é o primeiro 
    elemento na lista, em seguida, o numero 1 é adicionado aos outros subconjuntos existentes('[]', e '[2]'), 
    resultando em '[[1], [2, 1]]' e o processo se repete para os outros numeros também."""
    
    return result 

# Exemplo de uso:

nums = [1, 2]
resultado = subconjuntos(nums)
print(resultado)    