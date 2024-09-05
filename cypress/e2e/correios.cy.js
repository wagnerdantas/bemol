describe('Automação de Busca no site dos Correios', () => {
  
  const url = 'http://www.buscacep.correios.com.br/app/endereco/index.php';

  beforeEach(() => {
    cy.visit(url); // Visita a página dos Correios
  });

  it('Busca por CEP "69005-040" (Caminho Feliz)', () => {
    cy.get('#endereco').type('69005-040'); // Preenche o campo de busca
    cy.get('#tipoCEP').select('Todos'); // Seleciona o tipo de busca
    cy.get('#captcha').should('be.visible'); // Aguarda o campo CAPTCHA estar visível
    cy.wait(20000); // Aguarda 20 segundos para você digitar o CAPTCHA manualmente
    cy.get('#btn_pesquisar').click(); // Tenta clicar no botão após o CAPTCHA
    cy.get('tbody > tr > [data-th="Logradouro/Nome"]').should('contain', 'Rua Miranda Leão');
    cy.get('tbody > tr > [data-th="Bairro/Distrito"]').should('contain', 'Centro');
    cy.get('tbody > tr > [data-th="Localidade/UF"]').should('contain', 'Manaus/AM');
    cy.get('tbody > tr > [data-th="CEP"]').should('contain', '69005-040');
  });

  // Cenário 1: Entrada Inválida (CEP Inexistente)
  it('Busca por CEP inexistente "00000-000"', () => {
    cy.get('#endereco').type('00000-000'); // Preenche com CEP inexistente
    cy.get('#tipoCEP').select('Todos'); // Seleciona o tipo de busca
    cy.get('#captcha').should('be.visible'); // Aguarda o campo CAPTCHA estar visível
    cy.wait(20000); // Aguarda 20 segundos para você digitar o CAPTCHA manualmente
    cy.get('#btn_pesquisar').click(); // Tenta clicar no botão após o CAPTCHA
    cy.get('.msg-erro').should('contain', 'CEP não encontrado'); // Valida mensagem de erro
  });

  // Cenário 2: Validação de Campos Obrigatórios (Campo CEP Vazio)
  it('Busca com campo CEP vazio', () => {
    cy.get('#tipoCEP').select('Todos'); // Seleciona o tipo de busca
    cy.get('#captcha').should('be.visible'); // Aguarda o campo CAPTCHA estar visível
    cy.wait(20000); // Aguarda 20 segundos para você digitar o CAPTCHA manualmente
    cy.get('#btn_pesquisar').click(); // Tenta clicar no botão após o CAPTCHA
    cy.get('.msg-erro').should('contain', 'Informe o CEP'); // Valida mensagem de erro
  });

  // Cenário 3: Validação de Campos Obrigatórios (Tipo de Endereço não selecionado)
  it('Busca sem selecionar o tipo de endereço', () => {
    cy.get('#endereco').type('69005-040'); // Preenche o campo de busca
    cy.get('#captcha').should('be.visible'); // Aguarda o campo CAPTCHA estar visível
    cy.wait(20000); // Aguarda 20 segundos para você digitar o CAPTCHA manualmente
    cy.get('#btn_pesquisar').click(); // Tenta clicar no botão após o CAPTCHA
    cy.get('.msg-erro').should('contain', 'Selecione o tipo de endereço'); // Valida mensagem de erro
  });
});