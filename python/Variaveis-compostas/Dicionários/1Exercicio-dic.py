def ini():
    print('-'*30)
 
ini()    
print("SITUAÇÃO DO ALUNO")
ini()
          
aluno = {}

aluno['nome'] = input("Digite o seu nome: ")
aluno['nota'] = float(input("Digite sua nota: "))

if aluno['nota'] <  7:
    print("A situação e igual a: reprovado(a)")
else:
    print("A situação e igual a: aprovado(a)")