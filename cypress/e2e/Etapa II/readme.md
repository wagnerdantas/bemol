# Etapa II - Automação de Teste Web I 🌐

# Desafio

Nesta segunda etapa, o objetivo é demonstrar seu domínio na automação de testes web. A aplicação alvo para este desafio é o site [buscacep.correios.com.br](https://buscacep.correios.com.br/).

### Cenários a Serem Automatizados

1. **Realizar a busca com o valor “69005-040”** 🔍
2. **Realizar a busca com o valor “Lojas Bemol”** 🏢

## Desafios Técnicos

Durante o desenvolvimento dos testes, enfrentamos vários desafios técnicos:

- **Mudança na URL**: Anteriormente, a URL usada para testes não possuía CAPTCHA. No entanto, houve uma mudança recente onde essa URL antiga redireciona para uma nova URL que inclui um CAPTCHA. Isso trouxe novos desafios na automação.
- **Bloqueio por Requisições**: O site agora bloqueia rapidamente quando se realiza poucas requisições de teste. Esse comportamento não era observado anteriormente e foi uma nova dificuldade a ser enfrentada.