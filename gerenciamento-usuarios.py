# Gerenciamento de Usuários

usuarios = {}

# Funções auxiliares
def obterOpcao():
  info = """
  Opções:
  1 - Listar usuários cadastrados (F2)
	2 - Cadastrar usuário (F3)
	3 - Remover usuário (F4)
	4 - Sair (Encerra programa)
  """
  print(info)
  
  return int(input("Escolha uma opção: "))

def listarUsuarios():
  if usuarios:
    count = 0
    for usuario in usuarios.keys():
      count+=1
      print(count, "-", usuario)
  else:
      print("Não há usuários cadastrados.")
  main()
  
def cadastrarUsuario():
  email = input("Digite o email: ")
  senha = input("Digite a senha: ")
  try:
    validarCadastro(email, senha)
    usuarios[email] = senha
    print("Usuario cadastrado com sucesso!")
  except Exception as e:
    print(e)
  main()

def validarCadastro(email, senha):
  if email in usuarios.keys():
     raise Exception("Usuario já cadastrado. ")
  validarEmail(email)
  validarSenha(senha)

def validarEmail(email):
  emailValido = False
  if "@" in email:
    if  "." in email[email.index("@"): -1]:
      emailValido = True
  if not emailValido:
    raise Exception("Email invalido. ")
    
def validarSenha(senha):
  if len(senha) < 6:
    raise Exception("Senha deve conter mais de seis caracteres. ")
    
  if not any(char.isdigit() for char in senha):
    raise Exception("Senha deve conter pelo menos um número. ")
          
  if not any(char.isupper() for char in senha):
    raise Exception('Senha deve conter pelo menos uma letra maiuscula')
           
  if not any(char.islower() for char in senha):
    raise Exception('Senha deve conter pelo menos uma letra minuscula')

def removerUsuario(email):
  
  for usuario in usuarios.keys():
    if usuario == email:
      usuarios.pop(usuario)
      print("Usuario removido.")

# Main
def main():
  opcao = obterOpcao()
  if opcao == 1:
    listarUsuarios()
  elif opcao == 2:
    cadastrarUsuario()
  elif opcao == 3:
    email = input("Digite o email: ")
    removerUsuario(email)

main()