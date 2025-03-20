import json

# Função para carregar o conteúdo do arquivo JSON
def carregar_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar as atualizações no arquivo JSON
def salvar_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        # Passando ensure_ascii=False para garantir que os acentos sejam preservados
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Função principal para adicionar novas informações de um membro
def adicionar_informacoes(nome_arquivo):
    dados = carregar_json(nome_arquivo)

    # Obtendo informações via input
    nome = input("Digite o nome do novo membro: ")
    funcao = input(f"Digite a função de '{nome}': ")
    descricao = input(f"Digite a descrição de '{nome}': ")
    rosto = input(f"Digite o caminho da imagem de rosto de '{nome}': ")
    linkedin = input(f"Digite o LinkedIn de '{nome}' (ou deixe vazio): ")

    # Criando o novo membro como um dicionário
    novo_membro = {
        "nome": nome,
        "funcao": funcao,
        "descricao": descricao,
        "rosto": rosto,
        "linkedin": linkedin
    }

    # Adicionando o novo membro à lista de membros
    dados.append(novo_membro)

    # Salvando as atualizações no arquivo JSON
    salvar_json(nome_arquivo, dados)

    print("Informações do novo membro adicionadas com sucesso!")

# Nome do arquivo JSON
while True:
    nome_arquivo = input("Nome do arquivo: ")

    # Chamando a função principal
    adicionar_informacoes(nome_arquivo)
