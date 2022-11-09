FROM python:3.8-slim

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["yacron", "-c", "crontab.yml"]