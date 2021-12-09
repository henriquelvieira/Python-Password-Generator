import random
import string

def passwordGenerator(vTamanhoSenha):
    '''
    Função para Geração de senhas aleatórias utilizando Letras (Caixa alta e Baixa) + Número + Caracteres especiais

    Args:
        vlength (str): Tamanho da senha que será gerada

    Return:
        (str) Senha gerada
    '''
    vLower = string.ascii_lowercase #LISTAR TODAS AS LETRAS EM CAIXA BAIXA
    vUpper = string.ascii_uppercase #LISTAR TODAS AS LETRAS EM CAIXA ALTA
    vDigits = string.digits  #LISTAR TODOS OS NUMEROS
    vSymbols = string.punctuation #LISTAR TODOS OS CARACTERES ESPECIAIS 
    vAll = vLower + vSymbols + vUpper + vDigits #JUNÇÃO DE TODOS OS TIPOS DE CARACTERES
    # print(f'lower {lower}')
    # print(f'upper {upper}')
    # print(f'digits {digits}')
    # print(f'symbols {symbols}')
    # print(f'all {all}')
    
    vLength = vTamanhoSenha #TAMANHO DA SENHA QUE SERÁ GERADA
    vPassword = "".join(random.sample(vAll, vLength))
    return vPassword


print (f'Senha: {passwordGenerator(15)}')

