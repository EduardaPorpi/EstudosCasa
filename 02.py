# usando for:
# num = int(input("Digite um número: "))
# for x in range(num+1):
#    for y in range(1, x+1):
#        print(y, end="")
#    print()

# usando while:
num = int(input("Digite um número: "))
x = 0
while x <= num:
    y = 1
    while y <= x:
        print(y, end="")
        y += 1
    print()
    x += 1
