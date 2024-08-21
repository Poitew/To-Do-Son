FROM python:3.12-alpine

WORKDIR /to-do-son

RUN pip install art

COPY . .

CMD ["python3", "main.py"]