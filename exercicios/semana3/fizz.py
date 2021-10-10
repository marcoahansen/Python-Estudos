def main():
    numero= float(input("Digite um número para saber se é divisível por 3:"))
    
    resto3 = numero % 3
 
    if(resto3 == 0):
        print("Fizz")
    else:
        print(int(numero))
main()