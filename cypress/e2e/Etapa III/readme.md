# Etapa III - Automação de Teste Web II

# 🧪 Desafio de Automação - Trivago

## 🎯 Objetivo

Nesta terceira etapa do desafio, queremos aprofundar nosso entendimento e compreender como seria sua construção em métodos de validação. O objetivo é automatizar um fluxo de busca no site Trivago, extraindo informações sobre o primeiro hotel listado após ordenar as opções por "Avaliações e Sugestões".

## 🌐 Aplicação Alvo

- [trivago.com.br](https://www.trivago.com.br/)

## 📝 Cenário de Teste

### 🚀 Fluxo Definido para Automação

1. 🖥️ Acessar o site do Trivago.
2. 🔍 Pesquisar por "Manaus".
3. 📊 Ordenar as opções listadas por "Avaliações e Sugestões".
4. 🏨 Verificar o nome do primeiro hotel na lista.
5. ⭐ Verificar a avaliação do hotel.
6. 💵 Verificar o valor da estadia.

## 🤖 Automação

A automação foi realizada utilizando Cypress, um framework popular para automação de testes end-to-end. O fluxo descrito acima foi implementado conforme o código abaixo:

```jsx

describe('Automação de Busca Trivago', () => {

  const url = 'https://www.trivago.com.br/';

  beforeEach(() => {
    cy.visit(url); // Visita a página da Trivago
  });

  it('Busca por localidade e extrai dados do primeiro hotel', () => {
    cy.wait(10000);

    // Digita o texto no campo de pesquisa
    cy.get('[data-testid="search-form-destination"]').type('Manaus');

    // Aguarda o carregamento das sugestões
    cy.get('[aria-selected="true"] > [data-testid="ssg-element"] > .Suggestion_wrapper__wXhL2 > .Suggestion_textSection__ihJDz > .Suggestion_suggestionHighlight__8bFMG').should('be.visible');

    // Seleciona a sugestão correta
    cy.get('[aria-selected="true"] > [data-testid="ssg-element"] > .Suggestion_wrapper__wXhL2 > .Suggestion_textSection__ihJDz > .Suggestion_suggestionHighlight__8bFMG').contains('Manaus').click();

    // Aguarda um pouco para garantir que a página esteja pronta para a próxima ação
    cy.wait(10000);

    // Verifica se o botão de pesquisa está visível e clicável
    cy.get('.AnimatedContent_content__Ox3mR > span').should('be.visible').click({ force: true });

    cy.wait(10000);
    cy.get('[data-testid="sorting-selector-select"]').select('Avaliação e sugestões');
    cy.wait(10000);

    // Extração dos dados do primeiro hotel
    cy.xpath('//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[1]/div/article/div[2]/div[1]/section/h2/button/span')
      .invoke('text')
      .then(text => {
        cy.log(`Nome do Hotel: ${text}`);
      });

    cy.xpath('//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[1]/div/article/div[2]/div[1]/button/span/span/span/strong/span')
      .invoke('text')
      .then(text => {
        cy.log(`Avaliação: ${text}`);
      });

    cy.xpath('//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[1]/div/article/div[2]/div[2]/div/div[1]/span/b')
      .invoke('text')
      .then(text => {
        cy.log(`Valor: ${text}`);
      });
  });

});

```

## ⚠️ Desafios Encontrados

Durante o desenvolvimento da automação, encontrei dificuldades em identificar os seletores corretos dos elementos da lista de resultados, devido à estrutura dinâmica e complexa da página. Para superar esse obstáculo, utilizei o XPath do Cypress, que me permitiu acessar os elementos necessários para extrair os dados do primeiro hotel listado.

## ▶️ Como Executar o Teste

Para abrir o Cypress e executar o teste, utilize o comando abaixo:

```bash
npx cypress open

```
