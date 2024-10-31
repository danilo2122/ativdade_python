print("escolha a operação desajada")
print("+ para soma")
print("- para subtracao")
print("* para multiplicao")
print("/ para divisao")

opcao=(input("\n qual operação voce deseja? "))
if opcao == "+":
    valor1=(float(input("Insira o primeiro valor: ")))
    valor2=(float(input("insira o segundo valor: ")))
    adicao=(valor1+valor2)
    print("a soma entre", valor1, "e" , valor2, "é:",adicao) 


if opcao == "-":
    b1=(float(input("Insira o primeiro valor: ")))
    b2=(float(input("insira o segundo valor: ")))
    sub=(b1-b2)
    print("a soma entre", b1, "e" , b2, "é:",sub) 


if opcao == "*":
    c1=(float(input("Insira o primeiro valor: ")))
    c2=(float(input("insira o segundo valor: ")))
    mult=(c1*c2)
    print("a soma entre", c1, "e" , c2, "é:",mult) 


if opcao == "/":
    d1=(float(input("Insira o primeiro valor: ")))
    d2=(float(input("insira o segundo valor: ")))
    div=(d1/d2)
    print("a soma entre", d1, "e" ,d2, "é:",div) 