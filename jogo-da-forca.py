# Jogo da Forca

import random

palavras = ["amor", "baixinho", "coracao", "docinho", "escola", "feijao", "gente", "humano"]
niveis = [1, 2]

# Funções auxiliares
def obterNivelDoJogo(niveis):
  info = """
  Niveis do jogo:
  1 - Palavra aleatória
  2 - Escolha da primeira letra da palavra
  """
  print(info)
  
  nivel = int(input("Escolha um nível: "))
  
  if nivel not in niveis:
    print("Encerrando.")
  else:
    return nivel

def obterPalavra(nivel):
  if nivel == 1:
    return random.choice(palavras)
  else:
    letra = input("Digite a letra: ").lower()
    for i in palavras:
      if i[0] == letra:
        return i
    return None

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

def obterQuantidadeChances(palavra):
  return len(palavra) + 3

# Main
def main():
  nivelEscolhido = obterNivelDoJogo(niveis)
  
  nivelValido = nivelEscolhido in niveis
  
  if nivelValido:
    palavraInicial = obterPalavra(nivelEscolhido)
    palavraMascarada = obterStringMascarada(palavraInicial)
    quantidadeCaracteresUnicos = obterQtdCaracteresNaString(palavraInicial)
    adivinhouPalavra = False
    erros = 0
    acertos = 0
    chances = obterQuantidadeChances(palavraInicial)
    letrasUtilizadas = []
    
    print("Palavra: ", palavraMascarada)
    
    while not adivinhouPalavra:

      if erros < chances:
        letra = input("Digite uma letra: ").lower()

        if letra.isalpha() and len(letra) == 1:

          if letra in letrasUtilizadas:
            print("A letra já foi utilizada!")
          else:
            letrasUtilizadas.append(letra)
            
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
              print("A palavra não contém essa letra. Chances: ", erros, "/", chances)
        else:
          print("Não é uma letra.")
      else:
          print("Não há mais chances!")

main()