def valida_usuario(user):
    if len(user) > 30 or len(user) < 1:
        print("O usuário deve conter no máximo 30 caracteres e no mínimo 1! ")
        return False
    if not user[0].isupper():
        print("O usuário deve conter a primeira letra maiúscula! ")
        return False
    for char in user:
        if not (char.isalpha() or char.isdigit()):
            print("O usuário não deve conter caracteres especiais ou espaços!")
            return False
    return True

def valida_senha(senha):
    if len(senha) < 10:
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    special_chars = ["@", "$", "!", "%", "*", "?", "&"]
    if not any(char in special_chars for char in senha):
        return False
    return True

def valida_mensagem(mensagem):
    if len(mensagem) > 70:
        print("Mensagem muito longa. Por favor, tente novamente: ")
        return False
    return True

def obter_usuario():
    usuario = input("Digite o usuário (deve ter a primeira letra maiúscula, sem caracteres especiais, sem espaços e no máximo 30 caracteres): ")
    while not valida_usuario(usuario):
        usuario = input("Usuário inválido! Digite o usuário novamente: ")
    return usuario

def obter_senha():
    senha = input("Digite a senha (deve ter pelo menos 10 caracteres, um caracter especial, um número, ao menos uma letra maiúscula): ")
    while not valida_senha(senha):
        senha = input("Senha inválida! Digite a senha novamente: ")
    return senha

def obter_mensagem():
    mensagem = input("Digite a mensagem que quer criptografar (até 70 caracteres): ")
    while not valida_mensagem(mensagem):
        mensagem = input("Mensagem muito longa. Por favor, tente novamente: ")
    return mensagem

def exibir_usuario(usuario):
    print("Usuário: ", usuario)

def exibir_senha(senha):
    print("Senha: ", senha)

def exibir_mensagem_criptografada(mensagem_criptografada):
    print("Mensagem criptografada: ", mensagem_criptografada)
