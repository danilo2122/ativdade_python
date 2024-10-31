print("verifique qual é o maior número")
valor1=(int(input("Insira o primeiro valor: ")))
valor2=(int(input("Insira o segundo valor: ")))
valor3=(int(input("Insira o terceiro valor: ")))

if valor1>valor2 and valor1>valor3:
    print("o maior valor é", valor1)

elif valor2>valor3 and valor2>valor1:
    print("o maior valor é", valor2)

if valor3>valor1 and valor3>valor2:
    print("o maior valor é", valor3)