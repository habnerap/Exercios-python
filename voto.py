idade= int(input(("Qual idade do eleitor:")))
print(idade)

if (idade < 16):
    print("Não eleitor")
elif (idade >=18 and idade < 70):
    print("O eleitor é obrigado a votar")
elif ((idade >= 16 and idade < 18) or (idade >= 70)):
    print("Eleitor facultativo")