# Etapa IV - Automação de Teste de API 🤖

## Desafio

Nesta etapa final, o objetivo é demonstrar sua habilidade em automação de testes para APIs. A aplicação alvo para este desafio é o [serverest.dev](https://serverest.dev/).

### Cenários a Serem Automatizados

1. **Criação de um Usuário**: Automatize a criação de um usuário na API. 👤
2. **Verificar se o Usuário foi Criado**: Confirme que o usuário foi criado com sucesso. ✅
3. **Criação de um Produto**: Automatize a criação de um produto na API. 🛒
4. **Verificar se o Produto foi Criado**: Confirme que o produto foi criado com sucesso. ✅

## Requisitos

- **Python 3.12.5** 🐍
- PyCharm 💻
- `pytest` 🧪
- `requests` 🌐

## Instalação do PyCharm

1. **Baixar o PyCharm**:
    - Acesse o [site oficial do PyCharm](https://www.jetbrains.com/pycharm/download/).
    - Baixe a versão Community (gratuita) ou Professional (paga), conforme necessário.
2. **Instalar o PyCharm**:
    - Execute o instalador baixado e siga as instruções na tela para completar a instalação.
3. **Configurar o PyCharm**:
    - Abra o PyCharm e selecione **"Create New Project"**.
    - Escolha o diretório onde deseja criar o projeto e configure o ambiente virtual se necessário.

## Instalação do `pytest` / `requests`

1. **Abrir o Terminal**:
    - Abra o terminal integrado no PyCharm ou um terminal do sistema.
2. **Instalar o `pytest` e `requests`**:
    - Execute o seguinte comando para instalar as bibliotecas necessárias:
        
        ```bash
        pip install pytest requestsExecutar os Testes
        ```
        
3. **Executar no PyCharm**:
    - No PyCharm, clique com o botão direito no arquivo de teste e selecione **"Run 'pytest'"**.
4. **Executar no Terminal**:
    - Abra o terminal e navegue até o diretório do projeto.
    - Execute o comando:
        
        ```bash
        pytest
        ```