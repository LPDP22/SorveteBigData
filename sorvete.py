preco = 15
premium = 20

copo = input("Qual tipo de copo você vai querer? ")
if copo != "copinho" and "casquina":
        print("Nós só temos copinho e casquinha, por favor escolha entre as duas.")

if copo == "casquinha":
    preco = preco + 2
    premium = premium + 2
        
if copo == "copinho":
    preco = preco + 1
    premium = premium + 1
        
qtdcobertura = int(input("Quantas coberturas você quer no seu sorvete? "))
    
if qtdcobertura == 1:
    preco = preco + 1
    premium = premium + 1
    
    if qtdcobertura > 1:
        preco = preco + 2
        premium = premium + 2
        
precototal = input("Você quer o preço normal ou o Premium? ")
if precototal != "preco" or "premium":
    print("ERRO! Digite 'preco' ou 'premium'")
elif precototal == "preco":
    print(preco)
elif precototal == "premium":
    print(premium)
    
    
