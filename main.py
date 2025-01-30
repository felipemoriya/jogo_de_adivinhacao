alvo = 42

try:
  
  chute = int(input("Digite um número inteiro entre 0 e 100: "))
  if chute == alvo:
    print("parabens voce acertou!")

  else:
    print("Que pena, o numero era " + str(alvo))

except:
  
  print("Valor informado não é um numero inteiro")