# Imports
import funcoes
import random


# Processando os valores recebidos do usuário
def processar_PQZD(numeroP, numeroQ):
    funcoes.clear_screen()
    print("Numero P: ", numeroP)
    print("Numero Q: ", numeroQ)

    P = numeroP
    Q = numeroQ

    N = P * Q

    Z = (P - 1) * (Q - 1)

    print(f'Valor de N: {N}')
    print(f'Valor de Z: {Z}\n')

    # Gerar número aleatório para D
    D = gerar_numero_D_primo(Z)

    # D sendo primo de Z
    mdc = calcular_mdc(Z, D)    
    print("O MDC de", Z, "e", D, "é", mdc)

    criar_chaves(N, D, Z)


# Processo de criação das chaves públicas e privadas
def criar_chaves(N, D, Z):
    """ 
        É necessário encontrar um número E que satisfaça a 
        seguinte propriedade:

        (E * D) mod Z = 1 
        (E * base) mod modulo = 1
    """

    # Encontrar o valor de E
    E = encontrar_valor_de_E(base, modulo)

    def encontrar_valor_de_E(base, modulo):
        for E in range(1, modulo):
            if (E * base) % modulo == 1:
                return E
        return None  # Se não encontrar um inverso multiplicativo

    base = D
    modulo = Z

    if E is not None:
        print(f"O valor de E que satisfaz a equação ({base} * E) mod {modulo} = 1 é {E}.")
    else:
        print(f"Não foi encontrado um valor de E que satisfaça a equação.")

""" 
Chave pública é para encriptar      --> (E, N)  
Chave privada é para desencriptar   --> (D, N) 


As equeções são:
    TEXTO CRIPTOGRAFADO = (Texto original ^ E) mod N
    Texto original = (TEXTO CRIPTOGRAFADO ^ D) mod N


"""










# Gerar um número aleatório para D que seja primo em relação a Z
def gerar_numero_D_primo(Z):
    while True:
        D = random.randint(2, Z - 1)
        if calcular_mdc(Z, D) == 1:
            return D
    
# D precisa ser primo em relação à Z
def calcular_mdc(Z, D):
    while D:
        Z, D = D, Z % D
    return Z
