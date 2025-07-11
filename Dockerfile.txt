```dockerfile
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema e o Poetry
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 -

# Adiciona o Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Copia os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock* /app/

# Instala as dependências com o Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copia o código da aplicação
COPY . /app

# Expõe a porta 8000 para o FastAPI
EXPOSE 8000

# Comando para rodar a aplicação FastAPI com Uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```