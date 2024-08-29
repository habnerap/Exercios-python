#exercio fazer media ponderada , media simples e media harmonica

# Media simples 
valor1=float(input(("Adicione um valor:")))
valor2=float(input("Adicione um SEGUDO valor:"))
valor3=float(input("Adicione um TERCEIRO valor:"))
media=((valor2+valor1+valor3)/3)
print(f"A media simples dos valores {valor1} e {valor2} a media {media}" )

# Media Ponderada
pESO1=float(input("Adicione o valor do 1º peso:"))
pESO2=float(input("Adicione o valor do 2º peso:"))
pESO3=float(input("Adicione o valor do 3º peso:"))

media_pondera=(((pESO1*valor1)+(pESO2*valor2)+(pESO3*valor3))/(pESO3+pESO2+pESO1))
print(media_pondera)

# Media Harmonica
media_harmonica= 3/(1/valor1 + 1/valor2+ 1/valor3)
print=(media_harmonica)