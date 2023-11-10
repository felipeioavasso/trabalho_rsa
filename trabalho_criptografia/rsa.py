# Imports
import menus
import random
from tabela import ascii_table


class ChaveRSA:
    _contador_chaves = 0

    def __init__(self, P, Q, N, Z, D=None, E=None):
        self.P = P
        self.Q = Q
        self.N = N
        self.Z = Z
        self.D = D
        self.E = E
        self.ID = ChaveRSA._contador_chaves
        ChaveRSA._contador_chaves += 1

    def salvar_chaves(self):
        arquivo_nome = f"./chaves_{self.ID}.txt"
        with open(arquivo_nome, "w") as arquivo:
            arquivo.write(f"E: {self.E}  N: {self.N}  D: {self.D}")


    def criar_texto_criptografado(self, texto):
            texto_criptografado = []
            for char in texto:
                valor_criptografado = (ord(char) ** self.E) % self.N
                texto_criptografado.append(valor_criptografado)
            return TextoCriptografado(texto_criptografado, self.ID)


class TextoCriptografado:
    def __init__(self, texto_criptografado, chave_id):
        self.texto_criptografado = texto_criptografado
        self.chave_id = chave_id

    def salvar_texto_criptografado(self):
        arquivo_nome = f"./criptografados_{self.chave_id}.txt"
        with open(arquivo_nome, "w") as arquivo:
            for valor in self.texto_criptografado:
                arquivo.write(str(valor) + "")        


        

# Processando os valores recebidos do usuário
def processar_PQZD(numeroP, numeroQ):
    menus.clear_screen()
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
    print(f"O MDC de", Z, "e", D, "é", mdc)
    
    # 
    chave = ChaveRSA(P, Q, N, Z, D)
    global chave_rsa 
    chave_rsa = chave
    criar_chaves(chave)    

    return chave

    """ criar_chaves(N, D, Z)
    return N,D """


# Processo de criação das chaves públicas e privadas
def criar_chaves(chave):
    """ 
        É necessário encontrar um número E que satisfaça a 
        seguinte propriedade:

        (E * D) mod Z = 1 
        (E * base) mod modulo = 1
    """
   

    def encontrar_valor_de_E(chave):
        for chave.E in range(1, chave.Z):
            if (chave.E * chave.D) % chave.Z == 1:
                return chave.E
        return None  # Se não encontrar um inverso multiplicativo

    # Encontrar o valor de E
    chave.E = encontrar_valor_de_E(chave)

    if chave.E is not None:
        print(f"O valor de E que satisfaz a equação ({chave.D} * E) mod {chave.Z} = 1 é {chave.E}.")
        salvar_chaves(chave)
    else:
        print(f"Não foi encontrado um valor de E que satisfaça a equação.")
    
    return chave.E


# Converter a mensagem do emissor para decimais
def converter_para_decimais(frase_usuario):
    # Inicializar uma lista para armazenar os valores decimais dos caracteres
    frase_decimal = []

    # Converteer a frase do usuário em valores decimais usando a tabela ASCII
    for char in frase_usuario:
        if char in ascii_table:
            valor_decimal = ascii_table[char]
            frase_decimal.append(valor_decimal)

    print(f"A frase em ASCII é: {frase_decimal}")
    
    return frase_decimal


# Criptografar a mensagem do emissor
def encriptar(frase_decimal, chave):
    texto_criptografado = []

    for valor_decimal in frase_decimal:
        valor_criptografado = (valor_decimal ** chave.E) % chave.N
        texto_criptografado.append(valor_criptografado)

    print(f"O texto criptografado: {texto_criptografado}")
    salvar_texto_criptografado(texto_criptografado)

    return texto_criptografado

# Salvar o texto criptografado associado â chave
def salvar_texto_criptografado(texto_criptografado):
    with open("./criptografados.txt", "w") as arquivo:
        for valor in texto_criptografado:
            arquivo.write(str(valor) + "")

# Salvar as chaves
def salvar_chaves(chave):
    with open("./chaves.txt", "w") as arquivo:
        arquivo.write(f"E: {chave.E}  N: {chave.N}  D: {chave.D}") # está sobreescrevendo os registros anteriores, arrumar isso
# Salvar o texto criptografado associado â chave

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
