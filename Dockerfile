# Usamos uma imagem oficial do Python como base
FROM python:3.9-slim

# Definimos o diretório de trabalho dentro do container
WORKDIR /app

# Copiamos a nossa lista de requisitos para dentro do container
COPY requirements.txt .

# Instalamos todas as bibliotecas necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo o resto do nosso código (o dashboard.py, etc.) para o container
COPY . .

# Expomos a porta que o Streamlit usa
EXPOSE 8501

# O comando que será executado quando o container iniciar
CMD ["streamlit", "run", "dashboard.py"]