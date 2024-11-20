# Use uma imagem Python leve
FROM python:3.8-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências e instala as dependências
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho
COPY app/ .

# Expõe a porta em que a API vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
