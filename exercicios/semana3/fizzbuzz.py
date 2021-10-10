def main():
    numero= float(input("Digite um número para saber se é divisível por 3 e por 5:"))
    
    resto3 = numero % 3
    resto5 = numero % 5

    if(resto3 ==0):
        if(resto5 ==0):
            print("FizzBuzz")
        else:
            print(int(numero))
    else:
            print(int(numero))
main()