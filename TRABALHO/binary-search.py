"""
Exemplo de Busca Binária, utilizando o conceito de 'Divisão e Conquista'.
"""

def search(elements: list, element: int, end: int, start: int=0):
    #caso base
    while start <= end:
        mid = start + ((end - start) // 2)
        
        # caso loop
        if elements[mid] == element:
            return mid
        elif elements[mid] < element: 
            start = mid + 1
        else:
            end = mid - 1
    
    return "Elemento não encontrado"

elements = [4,6,9,12,14,18,21,24,38]
element = 4

result = search(elements, element, len(elements) -1)
print(f"O indice do elemento procurado é: {result}")