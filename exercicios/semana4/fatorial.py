n= int(input("Digite o valor de n: "))

sub = n - 1
fat = n

while n != 0:
    while sub != 1:
        fat = fat * sub
        sub = sub -1


print(fat)
