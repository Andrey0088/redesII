# Usar uma imagem base do Python
FROM python:3.9
# Instalar o Git
RUN apt-get update && apt-get install -y git

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# [cite_start]Clona o seu repositório do GitHub para dentro do contêiner [cite: 14]
# IMPORTANTE: Substitua 'SEU_USUARIO/SEU_REPOSITORIO.git' pelo link do seu repositório
RUN git clone https://github.com/Andrey0088/redesII.git

# Instala as dependências da aplicação
RUN pip install Flask psycopg2-binary
# Expõe a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]