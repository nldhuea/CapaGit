notas = {"um": 0, "cinco": 0, "dez": 0, "cinquenta": 0, "cem": 0}

sacar = int(input("Digite o valor que deseja sacar: "))

notas["cem"] = sacar // 100

notas["cinquenta"] = (sacar%100) // 50

notas["dez"] = (sacar%100%50) // 10

notas["cinco"] = (sacar%100%50%10) // 5

notas["um"] = sacar%100%50%10%5

print(notas)