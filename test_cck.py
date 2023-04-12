from att import  *

def test_valida_usuario_tamanho_maximo():
    assert valida_usuario("0123456789012345678901234567890123456789012345678901234567890123456789") == False

def test_valida_usuario_tamanho_minimo():
    assert valida_usuario("") == False

def test_valida_usuario_letra_maiuscula():
    assert valida_usuario("usuario") == False

def test_valida_usuario_caracteres_especiais():
    assert valida_usuario("usu@rio") == False

def test_valida_usuario_caracteres_validos():
    assert valida_usuario("Usuario123") == True

def test_valida_senha_tamanho_minimo():
    assert valida_senha("aA1$") == False

def test_valida_senha_letra_maiuscula():
    assert valida_senha("abcd1234$") == False

def test_valida_senha_letra_minuscula():
    assert valida_senha("ABCD1234$") == False

def test_valida_senha_caracter_especial():
    assert valida_senha("Abcd1234") == False

def test_valida_senha_caracteres_validos():
    assert valida_senha("Abcd1234$!") == True

def test_valida_mensagem_tamanho_maximo():
    assert valida_mensagem("01234567890123456789012345678901234567890123456789012345678901234567890123456789") == False

def test_valida_mensagem_tamanho_valido():
    assert valida_mensagem("0123456789") == True

