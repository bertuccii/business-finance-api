# Usar imagem oficial do Python
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY . /app

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "run.py"]
