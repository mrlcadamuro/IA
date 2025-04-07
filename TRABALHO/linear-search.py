"""
Exemplo de busca Linear.
"""
def search(elements: list, element) -> int:
    """
    Função que recebe uma lista e um valor, para que o algoritimo faça a busca.
    """
    for index,value in enumerate(elements):
        # caso base - condição que faz o loop parar.
        if value == element:
            return index

    return "Elemento não encontrado"


elements = [3,1,4,6,14]
result = search(elements, 1)

print(f"O indice do elemento procurado é: {result}")