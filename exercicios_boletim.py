
#Criar um boletim escolar . Com nomes , disciplinas , notas e semestre
notas = [7.8, 8.2 , 9.5 ,
          10 , 8 , 5, 7, 6]
disciplinas = ["matamática" , "português" ,  "filosofia",
                "física" , "geografia" , "química" ,"biologia", "Artes" ] 


for i in range(len(notas)):
    print(f"A nota da {disciplinas[i]} foi {notas[i]} ")