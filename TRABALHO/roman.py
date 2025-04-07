'''
Projeto 1 - Revisão 
Converter números inteiros para romanos.
'''


'''
int
float
str
bool 

list
tuple
dict
set
'''

def int_to_roman(number: int) -> str:
    """
    Função que recebe um valor int e retorna
    o valor em Romano como uma string.
    """
    symbols: dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "3",
    }

    roman = "" 

    for symbol in sorted(symbols.keys(), reverse=True):
        while number >= symbol:
            roman += symbols[symbol]
            number -= symbol
        
    return roman

number = int(input("Digite um valor inteiro: "))
roman = int_to_roman(number)

print(roman)