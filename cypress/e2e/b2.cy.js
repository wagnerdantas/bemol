describe('Busca no site dos Correios', () => {
  
  const url = 'http://www.buscacep.correios.com.br/app/endereco/index.php';
  const validCep = '69005-040';
  const invalidCep = '00000-000';
  const searchTerm = 'Lojas Bemol';
  const errorMsgSelector = '.msg-erro';

  const fillCepAndSearch = (cep) => {
    cy.get('#endereco').type(cep); // Preenche o campo de busca
    cy.get('#tipoCEP').select('Todos'); // Seleciona o tipo de busca
    cy.get('#captcha').should('be.visible'); // Aguarda o campo CAPTCHA estar visível
    cy.wait(20000); // Aguarda 20 segundos para você digitar o CAPTCHA manualmente
    cy.get('#btn_pesquisar').click(); // Tenta clicar no botão após o CAPTCHA
  };

  beforeEach(() => {
    cy.visit(url); // Visita a página dos Correios
  });

  // Cenário 1: Buscar por CEP "69005-040" (Caminho Feliz)
  it('Busca por CEP "69005-040" (Busca com sucesso)', () => {
    fillCepAndSearch(validCep);
    cy.get('tbody > tr > [data-th="Logradouro/Nome"]').should('contain', 'Rua Miranda Leão');
    cy.get('tbody > tr > [data-th="Bairro/Distrito"]').should('contain', 'Centro');
    cy.get('tbody > tr > [data-th="Localidade/UF"]').should('contain', 'Manaus/AM');
    cy.get('tbody > tr > [data-th="CEP"]').should('contain', validCep);
  });

  // Cenário 2: Buscar por "Lojas Bemol"
  it('Busca por "Lojas Bemol"', () => {
    fillCepAndSearch(searchTerm);
    cy.get('tbody > tr > [data-th="Logradouro/Nome"]').should('contain', 'Rua Miranda Leão, 41Lojas Bemol');
    cy.get('tbody > tr > [data-th="Bairro/Distrito"]').should('contain', 'Centro');
    cy.get('tbody > tr > [data-th="Localidade/UF"]').should('contain', 'Manaus/AM');
    cy.get('tbody > tr > [data-th="CEP"]').should('contain', validCep);
  });

  // Cenário 3: Buscar por CEP Inexistente "00000-000"
  it('Busca por CEP inexistente "00000-000"', () => {
    fillCepAndSearch(invalidCep);
    //cy.get(errorMsgSelector).should('contain', 'CEP não encontrado'); // Valida mensagem de erro
  });

  // Cenário 4: Buscar com Campo CEP Vazio
  it('Busca com campo CEP vazio', () => {
    cy.get('#tipoCEP').select('Todos'); // Seleciona o tipo de busca
    cy.get('#captcha').should('be.visible'); // Aguarda o campo CAPTCHA estar visível
    cy.wait(20000); // Aguarda 20 segundos para você digitar o CAPTCHA manualmente
    cy.get('#btn_pesquisar').click(); // Tenta clicar no botão após o CAPTCHA
    //cy.get(errorMsgSelector).should('contain', 'Informe o CEP'); // Valida mensagem de erro
  });

});

