# Dockerfile for app service

FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# # Install openpyxl
# RUN pip install openpyxl

COPY . .

CMD ["python", "scrape.py"]
