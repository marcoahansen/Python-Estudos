def main():
    numero= float(input("Digite um número para saber se é divisível por 5:"))
    
    resto5 = numero % 5

    if(resto5 == 0):
        print("Buzz")
    else:
        print(int(numero))
main()