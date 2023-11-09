import rsa
import funcoes

# Verificar se os números escolhidos são primos 
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Gerar dois números primos distintos
def gerar_dois_numeros_primos_distintos():
    import random

    while True:
        prime1 = random.randint(2, 99)
        prime2 = random.randint(2, 99)
        
        if prime1 != prime2 and is_prime(prime1) and is_prime(prime2):
            return prime1, prime2


def criptografar_frase():
    # Solicitando frase ao usuário
    frase_usuario = input("Digite a sua frase a ser criptografada: \n")
    print()

    # Perguntar ao usuário se deseja gerar P e Q automaticamente
    gerar_auto = input(f"Deseja gerar automaticamente os números P e Q?\n(S para Sim, N para Não): ").strip().lower()

    # Ponto de decisão para o usuário
    if gerar_auto == 's':
        # Gerar automaticamente os números P e Q
        numeroP, numeroQ = gerar_dois_numeros_primos_distintos()
    else:
        while True:
            numeroP = int(input("Digite o primeiro número (P): "))
            numeroQ = int(input("Digite o segundo número (Q): "))
            if is_prime(numeroP) and is_prime(numeroQ):
                break
            else:
                print("Certifique-se de que ambos os números são primos.")

    rsa.processar_PQZD(numeroP, numeroQ)
    input()

    funcoes.print_menu_final()

    
    
