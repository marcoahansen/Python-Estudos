def main():
    tamanho= int(input("Digite o tamanho de uma sequência de números a serem multiplicados: "))
    produto = 1
    i = 1 

    while i < tamanho:
        valor = int(input("Digite um valor a ser multiplicado: "))
        produto = produto * valor
        i = i + 1

    print("O produto dos valores digitados é: ", produto)

main()