print("veja se seu voto é obrigátorio,opcional ou proibido")
idade=int(input("digite sua idade: "))
if idade >=18:
    print("obrigatório")
elif idade <16:
    print("proibido")
elif idade >=16 and idade <=17:
    print("opcional")
    