FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install pandas matplotlib numpy

CMD ["python", "./WaitTimeAnalysis.py"]