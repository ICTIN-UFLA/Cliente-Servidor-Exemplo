# Usa uma imagem oficial do Python como base
FROM python:3.8

# Define o diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do diretório atual para o /app no container
COPY . /app

# Instala as dependências necessárias
RUN pip install -r requirements.txt

# Expõe a porta 5000 para comunicação com o mundo externo
EXPOSE 5000

# Define o comando padrão para iniciar o servidor
CMD ["python", "server.py"]