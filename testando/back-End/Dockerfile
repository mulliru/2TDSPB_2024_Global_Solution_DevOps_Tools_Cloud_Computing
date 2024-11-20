FROM python:3.11

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do back-end
COPY . .

# Expor a porta do Flask
EXPOSE 5000

# Comando para iniciar o servidor Flask
CMD ["python", "app.py"]
