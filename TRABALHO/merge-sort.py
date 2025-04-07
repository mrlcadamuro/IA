"""
Exemplo de Divisão e Conquista, com ordenação e mesclagem.
"""
def merge_sort(elements:list) ->list:
    """
    função recebe uma lista não ordenada, então utilizando o conceito
    de 'divisão e conquista', fará a divisão da lista em sublistas até
    que reste somente 1 elemento. Em paralelo invoca a função merge para fazer a mesclagem, 
    ja ordenando os elementos.
    """
    #TODO: caso base: Se o tamanho da lista for 1
    if len(elements) ==1:
        return elements
    
    #TODO: Encontrar o meio da lista (divisão inteira)
    mid = len(elements) // 2

    #TODO: Cada metade dividir ao meio até restar 1 elemento (caso base acionado)
    first = elements[:mid]
    second = elements[mid:]

    #TODO> Caso de loop: Cada vez que dividir, invoca a função merge
    first_half = merge_sort(first)
    second_half = merge_sort(second)

    return merge(first_half, second_half)

def merge(first: list, second:list):
    index1 = index2 = 0
    elements = []
    while index <len(first)



elements = [12,11,7,41,61,13,16,14]
print(merge_sort)
