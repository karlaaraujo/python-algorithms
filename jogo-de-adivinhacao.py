# Jogo de Adivinhacao

palavras = ["dragon", "game", "throne", "python", "word", "music"]

acertou = False

while(not acertou):
  tentativa = input("Digite a tentativa: ")

  if tentativa.lower() in palavras:
    print("Você acertou!")
    break
  else:
    print("Você errou. Tente novamente.")