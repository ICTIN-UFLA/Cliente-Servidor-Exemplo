# Projeto de Demonstração: Aplicação Dockerizada com Cliente Web, Servidor Web e MySQL

## Características do Projeto
Este projeto demonstra a orquestração de uma aplicação composta por três serviços principais utilizando Docker Compose:

- **Servidor Web (API)**: Uma aplicação Python que fornece uma API para acessar dados de usuários armazenados em um banco de dados MySQL.
- **Cliente Web**: Uma interface web em Python que interage com a API para exibir dados dos usuários.
- **Banco de Dados MySQL**: Um serviço de banco de dados que armazena informações sobre os usuários.

## Estrutura do Projeto

/your-project-directory\
|-- app/\
| |-- server.py\
| |-- web.py\
| |-- requirements.txt\
| |-- Dockerfile\
|-- db/\
| |-- init.sql\
|-- docker-compose.yml


### Descrições dos Arquivos
- **server.py**: Contém o servidor API que se conecta ao MySQL e oferece uma rota para recuperar dados de usuários.
- **web.py**: Um cliente web que exibe os usuários recuperados da API.
- **requirements.txt**: Lista todas as dependências Python necessárias para o servidor e o cliente web.
- **init.sql**: Script SQL para inicializar o banco de dados e preencher com dados de exemplo.
- **Dockerfile**: Define o ambiente Python necessário para rodar o servidor e o cliente web.
- **docker-compose.yml**: Configura e liga todos os serviços necessários para o projeto.

## Instruções de Configuração
1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/ICTIN-UFLA/Cliente-Servidor-Exemplo.git
   cd Cliente-Servidor-Exemplo

2. **Construir e Iniciar os Serviços**:

    docker-compose up --build

### Testando a Aplicação

## Testar a API
1. **URL para Teste: http://localhost:5000/**

2. **Ação: Acesse a URL em um navegador ou usando uma ferramenta como Postman para verificar se a lista de usuários é retornada corretamente.** 

## Testar o Cliente Web
1. **URL para Teste: http://localhost:8000/**

2. **Ação: Acesse a URL em um navegador para verificar se a interface do usuário exibe corretamente os dados dos usuários obtidos através da API.**

## Logs de Diagnóstico

Verifique os logs no terminal onde o docker-compose up está executando para identificar qualquer problema ou erro durante a execução dos serviços.


### Encerrando os Serviços

Para parar e remover os contêineres criados pelo Docker Compose, execute: \

docker-compose down

### Suporte

Se você encontrar problemas ou tiver dúvidas, não hesite em entrar em contato através de [bento.siqueira@ufla.br].