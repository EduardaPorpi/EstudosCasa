perg = "s"
while perg == "s":
    hora = int(input("Digite a hora: "))
    while hora > 24:
        hora = int(input("Dado incorreto. Digite a hora novamente: "))
    min = int(input("Digite os minutos: "))
    if hora > 12:
        hora -= 12
        print(f"São {hora}:{min} P.M")
    else:
        print(f"São {hora}:{min} A.M")
    perg = input("Deseja continuar calculando? ")
else:
    print("Obrigada!")
