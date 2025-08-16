# Usar uma imagem base do Python
FROM python:3.9-slim-bullseye
# Instalar o Git
RUN apt-get update && apt-get install -y git && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Clona o repositório
RUN git clone https://github.com/Andrey0088/redesII.git

# Define o diretório de trabalho para dentro do repositório clonado
WORKDIR /app/redesII

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]