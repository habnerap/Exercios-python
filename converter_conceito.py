# Eu quero criar um codigo , onde se adiona nota de 1 a 10  , que se converta em conceito "A"a "F"

nota_do_aluno =float(input("adicione a nota: "))

if nota_do_aluno>=10:
    conceito = "A++10"
elif nota_do_aluno<10 and nota_do_aluno>=9:
    conceito = "A"
elif nota_do_aluno<8 and nota_do_aluno>=6:
    conceito = "B"
elif nota_do_aluno<6 and nota_do_aluno>=4:
    conceito = "C"
elif nota_do_aluno<4 and nota_do_aluno>=2:
    conceito = "D"
else:
    conceito = "E"
print(f"Aluno tirou {conceito}!!!")
