def ini():
    print('=' * 30)
    
ini()
print("TABElA DE CLASSIFICADOS")
ini()

classi = ('1 lugar: flamengo', '2 lugar: plameiras', '3 lugar: cruzeiro', '4 lugar: mirassol', '5 lugar: fluminense', '6 lugar: botafogo', '7 lugar: bahia', '8 lugar: sao paulo', '9 lugar: gremio', '10 lugar: bragantino', '11 lugar: atletico-MG', '12 lugar: santos', '13 lugar: corinthias', '14 lugar: vasco da gama', '15 lugar: vitoria', '16 lugar: internacional', '17 lugar: ceara', '18 lugar: fortaleza', '19 lugar: juventude', '20 lugar: sport')

print("5 primeiros colocados")
for a in classi[:5]:
     print(a)
ini()
print("ultimos colocados")
for b in classi[-4:]:
    print(b)
ini()
alfabetico = sorted(classi)
print("ordem alfabetica")
for c in alfabetico:
    print(c)