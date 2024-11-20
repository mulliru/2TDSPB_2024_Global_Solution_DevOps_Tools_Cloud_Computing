# Global Solution 

Este repositório contém o código e os arquivos necessários para rodar a aplicação da "Global Solution", um projeto para mapear pontos de abastecimento de carros elétricos. A aplicação é composta por um front-end e um back-end que se comunicam para fornecer informações sobre os pontos de abastecimento disponíveis.

## Estrutura do Projeto

```
repositorio/
│
├── back-end/                 # Código do back-end com Flask
│   ├── app.py                # Código principal do Flask
│   ├── requirements.txt      # Lista de dependências do Python
│   └── Dockerfile            # Dockerfile para o back-end
│
├── front-end/                # Código do front-end
│   ├── index.html            # Página HTML principal
│   ├── script.js             # Lógica de interação do front-end
│   ├── style.css             # Estilo da página
│   └── Dockerfile            # Dockerfile para o front-end
│
├── docker/                   # Arquivos relacionados ao Docker e orquestração
│   ├── docker-compose.yml    # Arquivo para orquestrar os serviços
│   ├── nginx.conf            # Configuração do Nginx para o front-end
│
└── README.md                 # Instruções gerais do projeto
```

## Tecnologias Utilizadas

- **Back-end**: Flask (Python)
- **Front-end**: HTML, CSS, JavaScript
- **Banco de Dados**: MySQL
- **Servidor Web**: Nginx
- **Containerização**: Docker, Docker Compose

## Configuração e Execução

Siga as instruções abaixo para configurar e executar a aplicação usando Docker.

### Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Passos para Execução

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd repositorio
   ```

2. Navegue até o diretório `docker`:
   ```sh
   cd docker
   ```

3. Construa e inicie os contêineres:
   ```sh
   docker-compose up --build
   ```

4. Acesse a aplicação:
   - **Front-end**: Acesse `http://localhost:8080` no navegador.
   - **Back-end**: As APIs podem ser acessadas em `http://localhost:5000`.

## Endpoints da API

- `GET /points`: Retorna todos os pontos de abastecimento.
- `GET /points/<int:id>`: Retorna um ponto de abastecimento específico.
- `POST /points`: Adiciona um novo ponto de abastecimento.
- `PUT /points/<int:id>`: Atualiza um ponto de abastecimento existente.
- `DELETE /points/<int:id>`: Remove um ponto de abastecimento.

## Estrutura de Dados

Cada ponto de abastecimento possui as seguintes informações:
- **nome**: Nome do ponto de abastecimento.
- **rua**: Rua onde o ponto está localizado.
- **cidade**: Cidade do ponto.
- **estado**: Estado do ponto.
- **tipo_carregador**: Tipo do carregador disponível.
- **capacidade**: Capacidade de carga (em kW).

## Considerações Finais

Este projeto é uma solução desenvolvida para o Global Solution 2024 da FIAP, focada em auxiliar o mapeamento de pontos de abastecimento para carros elétricos. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para contribuir ou entrar em contato.

## Licença

Este projeto é licenciado sob os termos da licença MIT.

## Integrantes
 * **Murillo Ferreira Ramos**   RM: 553315  <br> 
 * **Pedro Luiz Prado**         RM: 553874  <br>
 * **William Kenzo Hayashi**    RM: 552659