P = 83
Q = 97

N = P * Q

Z = (P - 1) * (Q - 1)

print('Valor de N: ', N)
print('Valor de Z: ', Z)

D = 89

def calcular_mdc(numero1, numero2):
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1

numero1 = Z
numero2 = D

mdc = calcular_mdc(numero1, numero2)

print("O MDC de", numero1, "e", numero2, "é", mdc)


""" (E * D) mod Z = 1 """

def encontrar_inverso_multiplicativo(base, modulo):
    for E in range(1, modulo):
        if (E * base) % modulo == 1:
            return E
    return None  # Se não encontrar um inverso multiplicativo

base = D
modulo = Z

E = encontrar_inverso_multiplicativo(base, modulo)

if E is not None:
    print(f"O valor de E que satisfaz a equação ({base} * E) mod {modulo} = 1 é {E}.")
else:
    print(f"Não foi encontrado um valor de E que satisfaça a equação.")

""" 
Chave pública é (N, E)
Chave privada é (N, ) 

"""
print(f"A chave pública é ({N},{E})")
print(f"A chave privada é ({N},{D})")

# Limpar a tela do terminal
def clear_screen():
    print("\033c", end="")




texto = ["FATEC"]
    
"""
70^23 mod 187 = 9 --> texto criptografado = (Texto original ^ E) mod N (Chave pública)
9^7 mod 187 = 70 --> texto original = (Texto criptografado ^ D) mod N (chave privada)"""

""" Cifrar a palavra FATEC """

""" F = 70
A = 65
T = 84
E = 69
C = 67 """

""" # Chave pública
N = 8051
E = 1769

# Lista de letras
#minha_lista = ["FATEC"]
minha_lista = [70,65,84,69,67]
 """
