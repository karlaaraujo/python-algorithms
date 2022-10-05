# Jogo da Forca

def obterPosicoesDoCaractere(string, char):
  posicoes = [] 
  for i in range(len(string)):
      if string[i] == char:
          posicoes.append(i)
  return posicoes

def modificarCaractere(string, novoCaractere, index):
    if index < 0:  
        return novoCaractere + string
    if index > len(string):  
        return string + novoCaractere
    return string[:index] + novoCaractere + string[index + 1:]

def obterQtdCaracteresNaString(string):
    unique = []
    for char in string[::]:
      if char not in unique:
        unique.append(char)
    return len(unique)

def obterStringMascarada(string):
  stringMascarada = ""
  for i in range(0, len(string)):
    stringMascarada += "_"
  return stringMascarada

palavraInicial = "mystery"
palavraMascarada = obterStringMascarada(palavraInicial)
quantidadeCaracteresUnicos = obterQtdCaracteresNaString(palavraInicial)

adivinhouPalavra = False
erros = 0
acertos = 0

print("Palavra: ", palavraMascarada)

while not adivinhouPalavra:
  
  letra = input("Digite uma letra: ").lower()
  
  if letra in palavraInicial:
    
    acertos += 1
    
    for i in obterPosicoesDoCaractere(palavraInicial, letra):
      palavraMascarada = modificarCaractere(palavraMascarada, letra, i)
      
    palavraInicial = palavraInicial.replace(letra, "-")
    print("A palavra contém essa letra. Palavra: ", palavraMascarada)
    
    if acertos == quantidadeCaracteresUnicos:
      adivinhouPalavra = True
      print("Parabéns! Você adivinhou a palavra.")
  else:
    erros += 1
    
    print("A palavra não contém essa letra. Erros: ", erros)
    