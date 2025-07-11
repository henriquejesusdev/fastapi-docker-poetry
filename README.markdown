```markdown
# Aplicação FastAPI com Docker e Poetry

Este repositório contém uma aplicação FastAPI configurada para rodar em um contêiner Docker, utilizando Docker Compose para orquestração e Poetry para gerenciamento de dependências. O objetivo é fornecer um ambiente de desenvolvimento consistente e reprodutível.

## Pré-requisitos

- **Docker**: Certifique-se de que o Docker está instalado. [Instruções de instalação](https://docs.docker.com/get-docker/).
- **Docker Compose**: Certifique-se de que o Docker Compose está instalado. [Instruções de instalação](https://docs.docker.com/compose/install/).

## Como Executar

Siga os passos abaixo para clonar, construir e executar a aplicação:

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. **Construa e inicie os contêineres**:
   ```bash
   docker-compose up --build -d
   ```
   O parâmetro `-d` faz com que os contêineres rodem em segundo plano.

3. **Acesse a aplicação**:
   - Abra o navegador ou use um cliente HTTP (como Postman ou `curl`) e acesse:
     ```
     http://localhost:8000
     ```
     Você verá a mensagem: `{"message": "Bem-vindo à aplicação FastAPI!"}`
   - Para verificar a saúde da aplicação:
     ```
     http://localhost:8000/health
     ```
     Resposta: `{"status": "saudável"}`
   - Para acessar a documentação interativa do FastAPI:
     ```
     http://localhost:8000/docs
     ```

4. **Parar os contêineres**:
   ```bash
   docker-compose down
   ```

## Estrutura do Projeto

- `Dockerfile`: Configura a construção da imagem Docker com Python 3.11, Poetry e dependências do projeto.
- `docker-compose.yml`: Orquestra o contêiner, mapeia portas, configura volumes e define variáveis de ambiente.
- `main.py`: Código-fonte da aplicação FastAPI com endpoints de exemplo.
- `pyproject.toml`: Configuração do Poetry com dependências do projeto.
- `poetry.lock`: Garante versões consistentes das dependências (gerado pelo Poetry).
- `README.md`: Este arquivo com instruções.

## Notas

- **Volumes**: O volume `./:/app` sincroniza o código local com o contêiner, permitindo recarregamento automático com o Uvicorn.
- **Variáveis de Ambiente**: Configuradas no `docker-compose.yml` (`APP_ENV` e `LOG_LEVEL`) para personalizar o comportamento da aplicação.
- **Poetry**: Usado para gerenciar dependências de forma determinística. O `poetry.lock` garante consistência entre ambientes.

Se houver problemas, verifique os logs com:
```bash
docker-compose logs
```

## Licença

Este projeto é fornecido como exemplo educacional e não possui licença específica.
```