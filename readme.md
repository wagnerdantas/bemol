# Processo seletivo QA

# 🚀 Configuração do Ambiente para Cypress

Este projeto faz parte de um desafio para uma vaga de QA Pleno. Abaixo, você encontrará um guia passo a passo para configurar o ambiente necessário para rodar os testes automatizados usando Cypress.

## 🛠️ Pré-requisitos

Certifique-se de ter o [Node.js](https://nodejs.org/) instalado em sua máquina. Este projeto utiliza:

- **Node.js**: v20.17.0
- **Cypress**: v13.14.1
- **Visual Studio Code:** Editor de código recomendado para desenvolvimento e execução de testes.

### 🖥️ Instalando o Visual Studio Code

Para facilitar o desenvolvimento e a execução dos testes, recomenda-se usar o [Visual Studio Code](https://code.visualstudio.com/), um editor de código leve e poderoso.

1. Acesse o [site oficial do Visual Studio Code](https://code.visualstudio.com/).
2. Baixe e instale a versão apropriada para o seu sistema operacional (Windows, macOS, ou Linux).
3. Após a instalação, abra o VS Code e personalize-o conforme suas preferências.

**Extensões recomendadas:**

- **Cypress**: Facilita a integração e execução de testes Cypress dentro do VS Code.
- **ESLint**: Ajuda a manter a qualidade do código, verificando erros de sintaxe e problemas de estilo.
- **Prettier**: Formata automaticamente o código, mantendo um estilo consistente.

### 📥 Instalando o Node.js

Se ainda não tiver o Node.js instalado, siga os passos abaixo:

1. Acesse o site oficial do [Node.js](https://nodejs.org/) e baixe a versão 20.17.0 (ou a versão LTS mais próxima).
2. Siga as instruções do instalador para completar a instalação.
3. Após a instalação, verifique a versão do Node.js para garantir que está corretamente instalado:

```bash
node --version
```

Se a instalação foi bem-sucedida, você verá a versão do Node.js instalada.

## 📦 Instalação do Cypress

Siga os passos abaixo para configurar o Cypress no seu projeto:

1. **Instalar o Cypress**: Execute o comando abaixo para instalar o Cypress como uma dependência de desenvolvimento:
    
    ```bash
    npm install cypress --save-dev
    ```
    
2. **Verificar a versão do Cypress**: Confirme que a versão correta foi instalada:
    
    ```bash
    npx cypress --version
    ```
    
3. **Instalar Cypress Xpath**: Para suporte a seletores Xpath, adicione o pacote `cypress-xpath`:
    
    ```bash
    npm install cypress-xpath --save-dev
    ```
Vá em cypress>support>commands.js e adicione ao arquivo a seguinte linha: import 'cypress-xpath';

4. **Abrir o Cypress**: Use o comando abaixo para abrir o Cypress:
    
    ```bash
    npx cypress open
    ```
    

## 📂 Estrutura de Diretórios do Cypress

Após abrir o Cypress pela primeira vez, uma estrutura de diretórios será criada automaticamente. Abaixo estão os principais diretórios e suas funções:

- **cypress/downloads**: Este diretório é usado para armazenar arquivos que são baixados durante a execução dos testes, permitindo a validação de downloads como parte do fluxo de teste.
- **cypress/e2e**: Diretório onde os arquivos de teste (specs) são armazenados. Este é o local para criar e organizar seus testes End-to-End (E2E), que simulam o comportamento do usuário final.
- **cypress/fixtures**: Contém arquivos de dados que podem ser utilizados nos testes, como arquivos JSON para simular respostas de APIs ou qualquer outro tipo de dados estáticos que os testes possam precisar.
- **cypress/screenshots**: Armazena as capturas de tela que o Cypress tira automaticamente quando um teste falha, ou manualmente durante os testes, para ajudar na depuração e análise de falhas.
- **cypress/support**: Contém scripts que configuram o comportamento global do Cypress, como comandos customizados e configurações adicionais. Arquivos como `commands.js` podem ser usados para adicionar comandos personalizados que serão aplicados em todos os testes.

## 📋 Notas Adicionais

- Certifique-se de seguir os passos na ordem correta para evitar erros durante a configuração do ambiente.
- Lembre-se de ajustar as versões de acordo com os requisitos do projeto, se necessário.

---

Com isso, seu ambiente está pronto para rodar testes com o Cypress! 🚀